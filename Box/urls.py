from django.urls import path
from Box import views

urlpatterns = [
  path('', views.boxFileView),
]
