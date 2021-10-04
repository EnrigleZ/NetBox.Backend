import re
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from django.http.request import HttpRequest
import datetime
import json
from .models import GitCommit, GitCommitSerializer

def parseTimeStamp(ts_str: str):
    try:
        d = datetime.datetime.strptime(ts_str,"%Y-%m-%dT%H:%M:%S%z")
        return int(datetime.datetime.timestamp(d))
    except ValueError:
        return None

def webhook(request: HttpRequest):
    event = request.headers.get('X-GitHub-Event', '')
    if event == 'push':
        data = json.loads(request.body)
        ref_name = data.get('ref')
        commits = data.get('commits', [])
        print (f"Get {len(commits)} from {ref_name}")

        ignored_commits = []
        saved_commits = []
        for commit in commits:
            id = commit.get("id")
            message = commit["message"]
            committer = commit["committer"]["name"]
            url = commit["url"]
            timestamp = parseTimeStamp(commit["timestamp"])
            res = GitCommit.objects.filter(id=id)
            if len(res) or timestamp is None or id is None:
                ignored_commits.append(commit)
                continue
            commit_object = GitCommit(
                id=id,
                message=message,
                url=url,
                committer=committer,
                timestamp=timestamp,
            )
            commit_object.save()
            saved_commits.append(commit_object)

        return JsonResponse({
            'saved_commits': GitCommitSerializer(saved_commits, many=True).data,
            'ignored_commits': ignored_commits,
        })
    return HttpResponse('')

def getAllGitCommits(request: HttpRequest):
    objects = GitCommit.objects.all()
    return JsonResponse(GitCommitSerializer(objects, many=True).data, safe=False)

def checkCommit(request: HttpRequest):
    id = request.GET.get('id', None)
    qa = request.GET.get('qa', None)
    if id is None or qa is None:
        return HttpResponseBadRequest()
    try:
        object = GitCommit.objects.get(id=id)
    except GitCommit.DoesNotExist:
        return HttpResponseNotFound()

    object.qa_checked = qa
    object.save()

    return JsonResponse(GitCommitSerializer(object).data)
