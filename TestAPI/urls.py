from django.urls import path
from TestAPI import views

urlpatterns = [
  path('', views.test)
]
