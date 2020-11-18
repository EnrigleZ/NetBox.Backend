from django.urls import path
from TestAPI import views

urlpatterns = [
  path('test-struct/', views.TestStructViewSet.as_view({'get': 'retrieve', 'post': 'create'})),
  path('test-structs/', views.TestStructViewSet.as_view({'get': 'list'})),
]
