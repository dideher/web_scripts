from django.urls import path
from .views import HomePageView, upload_curriculum_status_file

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("upload_curriculum_status_file/",  upload_curriculum_status_file, name = 'upload_curriculum_status_file'),
]