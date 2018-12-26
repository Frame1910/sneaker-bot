import io
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/dpmei/Documents/GitHub/sneaker-bot/privKey/audioRecog-1b02c00756b5.json"

from pydub import AudioSegment

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()
print("Initialized SpeechClient")

print("Converting mp3 to WAV...")
sound = AudioSegment.from_mp3("C:/Users/dpmei/Documents/GitHub/sneaker-bot/audio.mp3").set_channels(1)
sound.export("C:/Users/dpmei/Documents/GitHub/sneaker-bot/audio.wav", format="wav")

# The name of the audio file to transcribe
file_name = "C:/Users/dpmei/Documents/GitHub/sneaker-bot/audio.wav"


#C:/Users/dpmei/Documents/GitHub/sneaker-bot/testAudio
# Loads the audio into memory
print("Loading audio into memory...")
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    sample_rate_hertz=22050,
    language_code='en-US')

# Detects speech in the audio file
print("Reading audio...")
response = client.recognize(config, audio)

print(response.results)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))

#os.remove("C:/Users/dpmei/Documents/GitHub/sneaker-bot/audio.mp3")
#os.remove("C:/Users/dpmei/Documents/GitHub/sneaker-bot/audio.wav")
