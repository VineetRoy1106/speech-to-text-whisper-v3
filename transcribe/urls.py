from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.upload_audio, name='transcribe1'),
    path('transcribe', views.transcribe_audio, name='transcribe1'),
    
]
