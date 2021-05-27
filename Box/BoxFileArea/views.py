from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import AnonymousUser
from rest_framework.response import Response
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework import status, permissions
from rest_framework.viewsets import ModelViewSet
from wsgiref.util import FileWrapper

import os, time

from .models import BoxFileArea

class BoxFileAreaViewSet(ModelViewSet):
    queryset = BoxFileArea.objects.all()
    permission_classes = (permissions.AllowAny, )

    def create(self, request):
        pass
    # def list(self, request):