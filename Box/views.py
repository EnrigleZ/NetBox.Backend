from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from Box.models import BoxFile
from Box.serializers import BoxFileSerializer


@api_view(['GET', 'POST'])
def boxFileView(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id is not None:
            boxfile = BoxFile.objects.filter(id=id)
            serializer = BoxFileSerializer(boxfile)
    if request.method == 'POST':
        # boxfile = BoxFile(request.POST, request.FILES)
        serializer = BoxFileSerializer(data=request.data)
        # print(request.data)
        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BoxFileViewSet(ModelViewSet):
    def list(self, request):
        boxfiles = BoxFile.objects.all()
        serializer = BoxFileSerializer(boxfiles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BoxFileSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request):
        id = request.GET.get('id', None)
        result = BoxFile.objects.get(id=id)
        serializer = BoxFileSerializer(result)
        return Response(serializer.data)

