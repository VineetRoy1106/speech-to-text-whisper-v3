from django.shortcuts import render
from transformers import pipeline
from pytube import YouTube
import os
import shutil
from .fb_scrape import extract_video_from_url
# print("Instantiating the transcriber")
# transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3", device="cuda")
# print("Loaded the transcriber")


import os
from uuid import uuid4

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
            
            audioname= uuid4().__str__()+".mp3"
            audio.name= audioname

            audio_file = Document.objects.create(
                                        name=audio.name,
                                        file=audio
                                        )
            
            os.rename(
                f"media/{audio.name}",
                f"media/{audioname}",
                
                )
            # print(f"audio_file: {audio_file.name}")

            # tc= TranscriberClass()


            # transcribed_text = transcriber(f"media/{audio.name}")['text']
            os.system(f"python whisper-diarization/diarize.py -a media/{audioname} --whisper-model large-v3")
            srt= f"media/{audioname[:-4]}.srt"
            txt= f"media/{audioname[:-4]}.txt"
            transcribed_text= ""
            with open(srt) as f:
                transcribed_text= f.read()

            print(f"Transcribed Text: {transcribed_text}")
            transcribed_text= transcribed_text.replace('\n', "<br>")
            os.remove(f"media/{audioname}")
            os.remove(srt)
            print(f"txt= {txt}")
            os.remove(txt)
            

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
            youtube_url = request.POST["youtube_url"]
            print(f"YouTube URL: {youtube_url}")

            # Download audio from YouTube video
            yt = YouTube(youtube_url)

            print("Bhai request aa gyi..........")

            audio_stream = yt.streams.filter(only_audio=True).first()
            media_directory = "media/"
            os.makedirs(media_directory, exist_ok=True)
            audio_file = f"{uuid4().__str__()}.mp3"

            # audio_stream.download(output_path="media/", filename=yt.title)
            audio_stream.download(output_path="media/", filename=audio_file)

            # Save the audio file in the Document model
            print("Bhai bahut badia..........")

            print("Bhai start transcribe..........")
            audio_file= f"media/{audio_file}"

            # Transcribe the audio
            # transcribed_text = transcriber(f"media/{audio_file}")['text']
            
            os.system(f"python whisper-diarization/diarize.py -a {audio_file} --whisper-model large-v3")
            srt= f"{audio_file[:-4]}.srt"
            txt= f"{audio_file[:-4]}.txt"
            transcribed_text= ""
            with open(txt) as f:
                transcribed_text= f.read()

            print(f"Transcribed Text: {transcribed_text}")
            transcribed_text= transcribed_text.replace('\n', "<br>")
            
            os.remove(audio_file)
            os.remove(srt)
            print(f"txt= {txt}")
            os.remove(txt)
            
            
            print("Bhai hogaya transcribe..........")

            return render(request, 'success.html', {
                "text": transcribed_text
            })
    except Exception as e:
        return HttpResponse(f"<h1>{e}</h1>")

























# ...MEGA NZ

def meganz_upload_video(request):
    return render(request, 'meganz.html')

def transcribe_meganz_video(request):
    print("Bhai request aa gyi..........")
    uid= uuid4().__str__()
    nz_folder= f"dummy_nz/{uid}"
    os.makedirs(nz_folder)
    try:
        if request.method == 'POST':
            print("inside post")
            mega_url = request.POST["mega_url"]
            print(f"MEGA.nz URL: {mega_url}")

            os.system(
                f"mega-get {mega_url} {nz_folder}"
            )
            
            audio_file= f'media/{uid}.mp3'
            
            # convert audio2video
            video_file= f'{nz_folder}/{os.listdir(nz_folder)[0]}'
            print(f"downloaded video file: {video_file}")
            clip= mp.VideoFileClip(video_file)
            clip.audio.write_audiofile(audio_file)
            
            
            
            
            
            os.system(f"python whisper-diarization/diarize.py -a {audio_file} --whisper-model large-v3")
            srt= f"{audio_file[:-4]}.srt"
            txt= f"{audio_file[:-4]}.txt"
            transcribed_text= ""
            with open(txt) as f:
                transcribed_text= f.read()

            print(f"Transcribed Text: {transcribed_text}")
            transcribed_text= transcribed_text.replace('\n', "<br>")
            
            os.remove(audio_file)
            os.remove(srt)
            print(f"txt= {txt}")
            os.remove(txt)
            
            
            print("Bhai hogaya transcribe..........")
            shutil.rmtree(nz_folder)
            return render(request, 'success.html', {
                "text": transcribed_text
            })
    except Exception as e:
        shutil.rmtree(nz_folder)
        return HttpResponse(f"<h1>{e}</h1>")




















import gdown
# ...GDrive

def gdrive_upload_video(request):
    return render(request, 'gdrive.html')

def transcribe_gdrive_video(request):
    print("Bhai request aa gyi..........")
    uid= uuid4().__str__()
    nz_folder= f"dummy_nz/{uid}"
    os.makedirs(nz_folder)
    try:
        if request.method == 'POST':
            print("inside post")
            file_id = request.POST["gdrivefileid"]
            file_id= file_id.replace('https://drive.google.com/file/d/', '')
            file_id= file_id[: file_id.index('/')]
            
            print(f"gdrive_file_id: {file_id}")
            url = f'https://drive.google.com/uc?id={file_id}'
            
            audio_file_mp4= f'{nz_folder}/{uid}.mp4'
            audio_file= f'{nz_folder}/{uid}.mp3'
            
            
            gdown.download(url, audio_file_mp4, quiet=False)
            
            
            
            os.system(f"python whisper-diarization/diarize.py -a {audio_file_mp4} --whisper-model large-v3")
            srt= f"{audio_file[:-4]}.srt"
            txt= f"{audio_file[:-4]}.txt"
            transcribed_text= ""
            with open(txt) as f:
                transcribed_text= f.read()

            print(f"Transcribed Text: {transcribed_text}")
            transcribed_text= transcribed_text.replace('\n', "<br>")
            
            
            
            print("Bhai hogaya transcribe..........")
            shutil.rmtree(nz_folder)
            return render(request, 'success.html', {
                "text": transcribed_text
            })
    except Exception as e:
        shutil.rmtree(nz_folder)
        return HttpResponse(f"<h1>{e}</h1>")














# ...FB

def fb_upload_video(request):
    return render(request, 'facebook.html')

def transcribe_fb_video(request):
    print("Bhai request aa gyi..........")
    uid= uuid4().__str__()
    nz_folder= f"dummy_fb/{uid}"
    os.makedirs(nz_folder)
    try:
        if request.method == 'POST':
            print("inside post")
            fb_url = request.POST["fb_url"]
            print(f"FB URL: {fb_url}")


            audio_file_mp4= f'{nz_folder}/{uid}.mp4'
            audio_file= f'{nz_folder}/{uid}.mp3'
            
            
            extract_video_from_url(url= fb_url, mp4_filename=audio_file_mp4)
            
            
            
            os.system(f"python whisper-diarization/diarize.py -a {audio_file_mp4} --whisper-model large-v3")
            srt= f"{audio_file[:-4]}.srt"
            txt= f"{audio_file[:-4]}.txt"
            transcribed_text= ""
            with open(txt) as f:
                transcribed_text= f.read()

            print(f"Transcribed Text: {transcribed_text}")
            transcribed_text= transcribed_text.replace('\n', "<br>")
            
            
            
            print("Bhai hogaya transcribe..........")
            shutil.rmtree(nz_folder)
            return render(request, 'success.html', {
                "text": transcribed_text
            })
    except Exception as e:
        shutil.rmtree(nz_folder)
        return HttpResponse(f"<h1>{e}</h1>")














































import moviepy.editor as mp

def upload_video(request):
    return render(request, 'video.html')
















   
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

            videoname= uuid4().__str__()+".mp4"
            video.name= videoname

            # Save the video file temporarily
            video_file = Document.objects.create(
                                        name=video.name,   
                                        file = video                                                                      
                                        )
            
            os.rename(
                f"media/{video.name}",
                f"media/{videoname}",
                
                )
            
            audio_file= f"media/{videoname}"

            
            os.system(f"python whisper-diarization/diarize.py -a {audio_file} --whisper-model large-v3")
            srt= f"{audio_file[:-4]}.srt"
            txt= f"{audio_file[:-4]}.txt"
            transcribed_text= ""
            with open(txt) as f:
                transcribed_text= f.read()
                
                

            print(f"Transcribed Text: {transcribed_text}")

            # Remove the video and audio files
            os.remove(audio_file)
            os.remove(txt)
            os.remove(srt)

            return render(request, 'success.html', {
                "text": transcribed_text
            })
    except Exception as e:
        return HttpResponse(f"<h1>{e}</h1>")
