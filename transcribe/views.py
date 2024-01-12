from django.shortcuts import render
from transformers import pipeline
from pytube import YouTube
import os

print("Instantiating the transcriber")
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3", device="cuda")
print("Loaded the transcriber")


import os

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods



from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField()


from django.shortcuts import render



def upload_audio(request):
    return render(request, 'upload_audio.html')

def transcribe_audio(request):
    try:
        if request.method == 'POST':
            audio = request.FILES["audio"]
            print(f"audio: {audio}")

            audio_file = Document.objects.create(
                                        name=audio.name,
                                        file=audio
                                        )
            
            
            transcribed_text = transcriber(audio.name)['text']
            
            print(f"Transcribed Text: {transcribed_text}")
            
            os.remove(audio.name)
            
            return render(request, 'success.html', {
                "text":transcribed_text
            })
    except Exception as e:
        return HttpResponse(f"<h1>{e}")


# ...

def youtube_upload(request):
    return render(request, 'youtube.html')

def transcribe_youtube(request):
    print("Bhai request aa gyi..........")
    try:
        if request.method == 'POST':
            print("inside post")
            # youtube_url = request.POST.get("youtube_url")
            youtube_url = request.POST["youtube_url"]
            print(f"YouTube URL: {youtube_url}")

            # Download audio from YouTube video
            yt = YouTube(youtube_url)
            print("Bhai request aa gyi..........")
            audio_stream = yt.streams.filter(only_audio=True).first()
            media_directory = "media/"
            os.makedirs(media_directory, exist_ok=True)
            audio_file_path = f"{yt.title.replace('|', '_')}.mp3"

            # audio_stream.download(output_path="media/", filename=yt.title)
            audio_stream.download(output_path="media/", filename=audio_file_path)

            # Save the audio file in the Document model
            print("Bhai bahut badia..........")

            print("Bhai start transcribe..........")

            # Transcribe the audio
            transcribed_text = transcriber(f"media/{audio_file_path}")['text']
            print("Bhai hogaya transcribe..........")

            # Remove the downloaded audio file
            os.remove(f"media/{audio_file_path}")

            return render(request, 'success.html', {
                "text": transcribed_text
            })
    except Exception as e:
        return HttpResponse(f"<h1>{e}")
