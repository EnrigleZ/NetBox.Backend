from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

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
        # files = request.FILES['file_part']
        # # print(files.size)
        # print(request.data)
        # return JsonResponse({})
        serializer = TestStructSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestStructViewSet(ModelViewSet):
    def list(self, request):
        queryset = TestStruct.objects.all()
        serializer = TestStructSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TestStructSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request):
        pass

    def retrieve(self, request):
        id = request.GET.get('id', None)
        result = TestStruct.objects.get(id=id)
        serializer = TestStructSerializer(result)
        return Response(serializer.data)
