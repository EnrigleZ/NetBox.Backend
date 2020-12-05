from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from TestAPI.models import TestStruct
from TestAPI.serializers import TestStructSerializer

import time
import json
import random

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


PRED_RESPONSE = {"auc": "0.916361454469064", "f1": "0.8721774856203779",
                 "precision": "0.8633524206142634", "recall": "0.8811848309756259"}


@api_view(['POST'])
def pred(request):
    body = json.loads(str(request.body))
    print(body)
    time.sleep(0.5)
    res = {"auc": str(random.random()), "f1": str(random.random()), "precision": str(random.random()), "recall": str(random.random()),
           "n_students": "123", "n_exercises": "1550", "total_num": "576681", "average_exercise": "25.321552",
           "model_name": body["model_name"], "dataset": body["dataset"]}
    return JsonResponse(res)


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
