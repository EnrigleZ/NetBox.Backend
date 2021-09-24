from django.urls import path, include
from .views import createImage, getImage

urlpatterns = [
    path('image', getImage),
    path('create', createImage),
]
