from django.http import HttpResponse
import os
from pathlib import Path

from django.http.response import HttpResponseBadRequest, JsonResponse
from rest_framework.status import HTTP_400_BAD_REQUEST
from configs import MEDIA_ROOT
from .models import IMAGE_DIR, ImageFile

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

def createImage(request):
    if request.method == 'POST':
        image_file_object = ImageFile(
            file_content=request.FILES.get('image')
        )
        image_file_object.save()
        return JsonResponse({'id': str(image_file_object.id)})