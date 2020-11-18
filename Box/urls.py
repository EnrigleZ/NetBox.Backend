from django.urls import path
from Box import views

urlpatterns = [
  path('box-file', views.BoxFileViewSet.as_view({'post': 'create', 'get': 'retrieve'})),
  path('box-files', views.BoxFileViewSet.as_view({'get': 'list'}))
]
