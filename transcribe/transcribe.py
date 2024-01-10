from yourproject.transcribe.forms import TranscribeForm
from transformers import Pipeline as pipeline
from django.shortcuts import render

def transcribe(request):
    if request.method == 'POST':
        form = TranscribeForm(request.POST, request.FILES)
        if form.is_valid():
            audio_file = request.FILES['audio_file']

            # Load model (outside the view function for efficiency)
            transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3", device="cuda")

            # Read audio file
            with open(audio_file.temporary_file_path(), 'rb') as f:
                audio = f.read()

            # Transcribe audio
            transcribed_text = transcriber(audio)["text"]

            return render(request, 'transcribe/results.html', {'text': transcribed_text})
    else:
        form = TranscribeForm()

    return render(request, 'transcribe/transcribe.html', {'form': form})
