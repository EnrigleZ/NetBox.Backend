from django.urls import path
from .views import createImage, getImage, getAllImages, getImageInfo

urlpatterns = [
    path('image', getImage),
    path('create', createImage),
    path('all', getAllImages),
    path('info', getImageInfo),
]
