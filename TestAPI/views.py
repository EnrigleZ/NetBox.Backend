from django.http import JsonResponse

from TestAPI.models import TestStruct
from TestAPI.serializers import TestStructSerializer


# Create your views here.
def test(request):
  return JsonResponse({'name': 123})

def createTest(request):
  item = TestStruct("placeholder", "placeholder")
  item.save()
