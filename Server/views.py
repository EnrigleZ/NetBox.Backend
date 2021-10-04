from django.http.response import HttpResponse, HttpResponseNotFound, JsonResponse

def webhook(response):
    return JsonResponse({'msg': 'ok'})