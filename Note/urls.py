from django.urls import path
from .views import createNote, getNotes

urlpatterns = [
    path('create', createNote),
    path('list', getNotes),
]
