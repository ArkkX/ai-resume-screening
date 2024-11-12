# resumes/urls.py
from django.urls import path
from .views import ResumeUploadView, JobMatchView

urlpatterns = [
    path('upload/', ResumeUploadView.as_view(), name='upload'),
    path('match/<int:candidate_id>/', JobMatchView.as_view(), name='match'),
]
