from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from TestAPI.models import TestStruct
from TestAPI.serializers import TestStructSerializer


# Create your views here.
def test(request):
  return JsonResponse({'name': 123})

@api_view(['GET', 'POST'])
def createTest(request):
  if request.method == 'GET':
    items = TestStruct.objects.all()
    serializer = TestStructSerializer(items, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    files = request.FILES['file_part']
    print(files.size)
    return JsonResponse({})
    print(request.data)
    serializer = TestStructSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)