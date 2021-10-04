from django.urls import path
from .views import checkCommit, getAllGitCommits, webhook

urlpatterns = [
    path('webhook', webhook),
    path('commits', getAllGitCommits),
    path('check-commit', checkCommit)
]
