from django.urls import path
from .views import createNote, getNote, getNotes

urlpatterns = [
    path('create', createNote),
    path('list', getNotes),
    path('', getNote),
]
