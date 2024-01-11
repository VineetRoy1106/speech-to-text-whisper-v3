from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.upload_audio, name='transcribe1'),
    path('transcribe', views.transcribe_audio, name='transcribe1'),
    path('youtube/', views.youtube_upload, name='youtube_upload'),
    path('youtube/transcribeyt', views.transcribe_youtube, name='transcribe_youtube'),
]
