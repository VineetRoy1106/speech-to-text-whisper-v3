# import gradio as gr
# from transformers import pipeline
# import numpy as np



# class TranscriberClass:
#     _instance= None

#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#             cls._instance.transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3", device="cuda")
#         return cls._instance
#     def transcribe(self, audio_file_path):
#         return self.transcriber(audio_file_path)['text']

# # # Load transcriber
# # transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3", device="cuda")
