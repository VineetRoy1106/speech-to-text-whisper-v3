from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.upload_audio, name='transcribe1'),
    path('transcribe', views.transcribe_audio, name='transcribe1'),
    path('youtube/', views.youtube_upload, name='youtube_upload'),
    path('youtube/transcribeyt', views.transcribe_youtube, name='transcribe_youtube'),
    path('meganzvideo/', views.meganz_upload_video, name='meganz_upload_video'),
    path('meganzvideo/transcribemeganz', views.transcribe_meganz_video, name='transcribe_meganz_upload_video'),
    path('fbvideo/', views.fb_upload_video, name='fb_upload_video'),
    path('fbvideo/transcribefb', views.transcribe_fb_video, name='transcribe_fb_upload_video'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('upload_video/video_to_audio', views.video_to_audio, name='video_to_audio')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)