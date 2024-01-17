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
    # form = AudioUploadForm()
    # return render(request, 'upload_audio.html', {'form': form})
    # form = AudioUploadForm()
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
            # print(f"audio_file: {audio_file.name}")

            # tc= TranscriberClass()


            transcribed_text = transcriber(f"media/{audio.name}")['text']

            print(f"Transcribed Text: {transcribed_text}")

            os.remove(f"media/{audio.name}")

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
            audio_file = f"{yt.title.replace('|', '_')}.mp3"

            # audio_stream.download(output_path="media/", filename=yt.title)
            audio_stream.download(output_path="media/", filename=audio_file)

            # Save the audio file in the Document model
            print("Bhai bahut badia..........")

            print("Bhai start transcribe..........")

            # Transcribe the audio
            transcribed_text = transcriber(f"media/{audio_file}")['text']
            print("Bhai hogaya transcribe..........")

            # Remove the downloaded audio file
            os.remove(f"media/{audio_file}")

            return render(request, 'success.html', {
                "text": transcribed_text
            })
    except Exception as e:
        return HttpResponse(f"<h1>{e}</h1>")


import moviepy.editor as mp

def upload_video(request):
    return render(request, 'video.html')

import re

def hi(request):
    try:
        if request.method == 'POST':
            video = request.FILES["video"]
            print(f"Video: {video}")
            

            # Save the video file temporarily
            video_file = Document.objects.create(
                                        name=video.name,   
                                        file = video                                                                      
                                        )
            
            print('starting video to audio')

            video_path = os.path.join('media', video.name)
            print(f"Video Path: {video_path}")
            print( f"media/{video.name}")

            # Convert the video to audio            
            clip = mp.VideoFileClip( f"media/{video.name}")
            print("Accessed video")

            clip.audio.write_audiofile(f"media/{video.name}")

            print("audio mein convert hogayi")
            # Transcribe the audio
            transcribed_text = transcriber(f"media/{video.name}")['text']
            
            print(f"Transcribed Text: {transcribed_text}")
            
            # Remove the video and audio files
            
            os.remove(f"media/{video.name}")
            
            return render(request, 'success.html', {
                "text":transcribed_text
            })
    except Exception as e:
        return HttpResponse(f"<h1>{e}</h1>")
   
import os
from django.http import HttpResponse
from django.shortcuts import render
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def video_to_audio(request):
    try:
        if request.method == 'POST':
            video = request.FILES["video"]
            print(f"Video: {video}")

            video = video.name.replace(' ', '_')

            # Save the video file temporarily
            video_file = Document.objects.create(
                                        name=video.name,   
                                        file = video                                                                      
                                        )
            
            video_path = f"media/{video.name}"

            print('Starting video to audio')

            print(f"media/{video.name}")

            # Convert the video to audio
            clip = VideoFileClip(video_path)
            audio = clip.audio

            # Write the audio file using 'mp3' codec
            audio.write_audiofile(f"{video_path}.mp3", codec='mp3')

            print("Audio conversion completed")

            # Transcribe the audio (you need to implement your transcriber function)
            transcribed_text = transcriber(f"{video_path}.mp3")['text']

            print(f"Transcribed Text: {transcribed_text}")

            # Remove the video and audio files
            os.remove(video_path)
            os.remove(f"{video_path}.mp3")

            return render(request, 'success.html', {
                "text": transcribed_text
            })
    except Exception as e:
        return HttpResponse(f"<h1>{e}</h1>")
