from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import AudioDataModel
# ... [other imports]
import __future__ 

from uuid import uuid4


from pydub import AudioSegment

from celery import shared_task
from django.utils import timezone

from transcribe import models

@shared_task
def process_uploaded_file(audio_data_id):
    """
    Call all other processing methods from this method
    """

    # Get Audio data model
    audio_data = models.AudioDataModel.objects.get(id=audio_data_id)

    # Convert uploaded file into MP3 format
    convert_into_mp3(audio_data)

    
   


def convert_into_mp3(audio_data):
    """
    Converts the uploaded file into MP3 format
    """

    uploaded_file_name = audio_data.uploaded_file.name
    file_extension = uploaded_file_name.split('.')[-1].lower()
    exported_file_name = None

    # Convert into MP3 format
    if file_extension != 'mp3':
        audio = AudioSegment.from_file(uploaded_file_name, file_extension)

        # Generate a unique name and then export as MP3
        exported_file_name = f'{str(uuid4())}.mp3'
        audio.export(exported_file_name, format='mp3')

    # Already an MP3 file
    else:
        exported_file_name = uploaded_file_name

   

    return







