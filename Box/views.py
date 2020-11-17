from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from Box.models import BoxFile
from Box.serializers import BoxFileSerializer


@api_view(['GET', 'POST'])
def boxFileView(request):
    if request.method == 'POST':
        boxfile = BoxFile(request.POST, request.FILES)
