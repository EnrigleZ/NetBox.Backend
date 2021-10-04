from django.http.response import HttpResponse, HttpResponseNotFound, JsonResponse
from django.http.request import HttpRequest
import datetime
from .models import GitCommit

def parseTimeStamp(ts_str: str):
    try:
        d = datetime.datetime.strptime(ts_str,"%Y-%m-%dT%H:%M:%S%z")
        return datetime.datetime.timestamp(d)
    except ValueError:
        return None

def webhook(request: HttpRequest):
    event = request.headers.get('X-GitHub-Event', '')
    if event == 'push':
        ref_name = request.body.get('ref')
        commits = request.body.get('commits', [])
        print (f"Get {len(commits)} from {ref_name}")

        ignored_commits = []
        saved_commits = []
        for commit in commits:
            id = commit.get("id")
            message = commit["message"]
            committer = commit["committer"]["name"]
            url = commit["url"]
            timestamp = (commit["timestamp"])
            if timestamp is None or id is None:
                ignored_commits.append(commit)
                continue
            commit_object = GitCommit(
                id=id,
                message=message,
                url=url,
                committer=committer,
                timestamp=timestamp,
            )
            # commit_object.save()
            saved_commits.append(commit)

        return JsonResponse({
            'saved_commits': saved_commits,
            'ignored_commits': ignored_commits,
        })
    return HttpResponse('')

# def