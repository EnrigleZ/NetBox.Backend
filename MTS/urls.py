from django.urls import path, include
from .views import getTree, getTrees, genereteTree

urlpatterns = [
    path('generate-random-tree/', genereteTree),
    path('trees/', getTrees),
    path('tree/', getTree)
]
