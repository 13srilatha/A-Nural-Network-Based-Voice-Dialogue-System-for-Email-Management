from transformers import pipeline, Wav2Vec2ForCTC, Wav2Vec2ProcessorWithLM
import sounddevice as sd
from lib import format_asr_result
import librosa
import sounddevice as sd
import speech_recognition as sr
from textblob import TextBlob

class ASRModule:
#
    def __init__(self):
        # asr_processor = Wav2Vec2ProcessorWithLM.from_pretrained('/mnt/c/Users/srila/OneDrive/Desktop/project2/blind-mailAI/notebooks/asr/models/wav2vec2LM')
        # self.pipe = pipeline('automatic-speech-recognition',
        #                      model=Wav2Vec2ForCTC.from_pretrained('/mnt/c/Users/srila/OneDrive/Desktop/project2/blind-mailAI/notebooks/asr/models/wav2vec2LM'),
        #                      tokenizer=asr_processor.tokenizer,
        #                      feature_extractor=asr_processor.feature_extractor,
        #                      decoder=asr_processor.decoder)
        self.beep, self.sr = librosa.load('/mnt/c/Users/srila/OneDrive/Desktop/project2/blind-mailAI/beep.mp3')
    def transcribe_audio(self, time=5):
        print('waiting for a reply ....')

        sd.play(self.beep, self.sr)

        recognizer = sr.Recognizer()

        # Use microphone as the audio source
        with sr.Microphone() as source:
            print("Speak something...")
            audio_data = recognizer.listen(source)
            print("listening")

            # Convert speech to text
            try:
              text = recognizer.recognize_google(audio_data)
              print("text:", text)
              print('Processing...')
              return format_asr_result(text)

            except sr.UnknownValueError:
                print("Sorry, could not understand audio.")
            except sr.RequestError as e:
                print("Error occurred:", str(e))

            return '0'
#
