from django.http import JsonResponse

# Create your views here.
def test(request):
  return JsonResponse({'name': 123})
