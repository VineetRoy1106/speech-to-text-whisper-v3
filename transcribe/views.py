from django.shortcuts import render
from transformers import pipeline

print("Instantiating the transcriber")
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3", device="cuda")
print("Loaded the transcriber")


import os

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods


# from transcribe import models
from django.db import models
# from transcribe import tasks

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
            
            
            transcribed_text = transcriber(audio.name)['text']
            
            print(f"Transcribed Text: {transcribed_text}")
            
            os.remove(audio.name)
            
            return render(request, 'success.html', {
                "text":transcribed_text
            })
    except Exception as e:
        return HttpResponse(f"<h1>{e}")
