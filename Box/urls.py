from django.urls import path
from Box import views

urlpatterns = [
  path('box-file', views.BoxFileViewSet.as_view({
    'post': 'create',
    'get': 'retrieve',
    'delete': 'destroy'
  })),
  path('box-file-content', views.BoxFileViewSet.as_view({
    'post': 'create_content'
  })),
  path('box-files', views.BoxFileViewSet.as_view({'get': 'list', 'delete': 'destroy_all'})),
  path('download', views.downloadBoxFile)
]
