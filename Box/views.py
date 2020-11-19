from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from wsgiref.util import FileWrapper

import os, time

from Box.models import BoxFile
from Box.serializers import BoxFileSerializer

class BoxFileViewSet(ModelViewSet):
    @classmethod
    def get_box_file_path(cls, boxfile: BoxFile) -> str:
        try:
            return boxfile.file_content.path
        except:
            return None

    @classmethod
    def _delete_box_file_from_disk(cls, boxfile: BoxFile):
        path = cls.get_box_file_path(boxfile)
        if path is not None:
            if os.path.isfile(path):
                os.remove(path)

    def list(self, request):
        boxfiles = BoxFile.objects.all()
        serializer = BoxFileSerializer(boxfiles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BoxFileSerializer(data=request.data)
        if serializer.is_valid():
            time.sleep(10)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request):
        id = request.GET.get('id', None)
        result = BoxFile.objects.get(id=id)
        serializer = BoxFileSerializer(result)
        return Response(serializer.data)

    def destroy(self, request):
        id = request.GET.get('id', None)
        boxfile = BoxFile.objects.get(id=id)
        serializer = BoxFileSerializer(boxfile)
        boxfile.delete()
        self._delete_box_file_from_disk(boxfile)
        return Response(serializer.data)

    def destroy_all(self, request):
        id = request.GET.get('id', None)
        boxfiles = BoxFile.objects.all()
        serializer = BoxFileSerializer(boxfiles, many=True)
        for boxfile in boxfiles:
            self._delete_box_file_from_disk(boxfile)
            boxfile.delete()
        # boxfiles.delete()
        return Response(serializer.data)

@api_view(['POST'])
def downloadBoxFile(request):
    id = request.POST.get('id', None)
    if id is not None:
        boxfile = BoxFile.objects.get(id=id)
        path = BoxFileViewSet.get_box_file_path(boxfile)
    if id is None or not path:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    name = boxfile.name
    wrapper = FileWrapper(open(path, 'rb'))
    response = HttpResponse(wrapper, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment;filename="%s"' % name
    response['Content-Length'] = os.path.getsize(path)

    return response