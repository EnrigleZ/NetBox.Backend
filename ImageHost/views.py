from django.http import HttpResponse
import os
from pathlib import Path

from django.http.response import Http404, HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.status import HTTP_400_BAD_REQUEST
from configs import MEDIA_ROOT
from .models import IMAGE_DIR, ImageFile
from .serializers import ImageFileSerializer

IMAGE_PATH = os.path.join(MEDIA_ROOT, IMAGE_DIR)
Path(IMAGE_PATH).mkdir(exist_ok=True)

# Create your views here.
def getImage(request):
    id = request.GET.get('id')
    if not id:
        return HttpResponseBadRequest('no id in request')
    filepath = os.path.join(IMAGE_PATH, f'{id}.png')
    with open(filepath, 'rb') as file:
        return HttpResponse(file.read(), content_type="image/png")

def getImageInfo(request):
    id = request.GET.get('id', None)
    try:
        image_file_object = ImageFile.objects.get(id=id)
    except ImageFile.DoesNotExist:
        return HttpResponseNotFound()
    serializer = ImageFileSerializer(image_file_object)
    return JsonResponse(serializer.data)

def createImage(request):
    if request.method == 'POST':
        image_file_object = ImageFile(
            file_content=request.FILES.get('image')
        )
        image_file_object.save()
        serializer = ImageFileSerializer(image_file_object)
        return JsonResponse(serializer.data)

def getAllImages(request):
    images = ImageFile.objects.all()
    serializer = ImageFileSerializer(images, many=True)
    return JsonResponse(serializer.data, safe=False)
