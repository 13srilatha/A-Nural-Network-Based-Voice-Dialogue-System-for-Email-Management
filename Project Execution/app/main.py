import os
import sounddevice as sd
from google.cloud import texttospeech
from graph import GraphDST
from asr import ASRModule
from myemail import EmailModule
from understanding import UnderstandingModule
import librosa
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f"{os.getcwd()}/data/tts_auth_key.json"
os.environ['TOKENIZERS_PARALLELISM'] = 'true'

"""
look for emails from Riccardo
close the email
read the email
reply to the email

"""


# wewe

# noinspect PyTypeChecker
class Speaker:

    def __init__(self):
        self.voice = texttospeech.VoiceSelectionParams(
            language_code="en", name='en-IN-standard-A'
        )

        self.client = texttospeech.TextToSpeechClient()
        # Select the type of audio file you want returned

        self.audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type

    def say(self, text):
        response = self.client.synthesize_speech(
            input=texttospeech.SynthesisInput(text=text), voice=self.voice, audio_config=self.audio_config
        )
        with open(f"temp.mp3", "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)

        audio, sr = librosa.load('temp.mp3')
        sd.play(audio, sr)
        sd.wait()


class App:
    def __init__(self):
        self.speaker = Speaker()
        self.speaker.say('loading forms, please wait')
        print('kk')
        self.understanding_module = UnderstandingModule()
        print('kkk')
        self.asr_module = ASRModule()
        print('kkkk')
        self.opened_mail = []
        self.mail_module = EmailModule()
        print('kkkkk')
        self.graph_module = GraphDST()
        print('kkkkkk')
        self.speaker.say('loading complete')
        # initialize graph

    def main_loop(self):
        self.graph_module.print_graph()
        if len(self.opened_mail) == 0:
            self.speaker.say('what do you want to do?')
            self.graph_module.exchange('System', 'what do you want to do?')

            text = self.asr_module.transcribe_audio(6)
            print("ldone")
            if not text:
                self.main_loop()
                return
            intent, slots = self.understanding_module.process(text)
            print(intent, slots)

            # add successor

            if intent == 'send_email' and len(self.opened_mail) == 0:
                self.speaker.say('send an email')
                self.graph_module.exchange('System', 'send an email')
                mail = {'object': None, 'person': None, 'body': None}
                for slots in slots:
                    if slot[0] == 'object':
                        mail['object'] = slot[1]
                    elif slot[0] == 'person':
                        mail['person'] = slot[1]
                self.graph_module.exchange('User', text, intent, slots)
                for field in mail.keys():
                    if mail[field] is None:
                        if field == 'person':
                            self.speaker.say('who should this be sent to?')
                            self.graph_module.exchange('System', 'who should it be sent to?')
                            mail['person'] = self.asr_module.transcribe_audio()
                            self.graph_module.exchange('User', mail['person'], None, [('person', mail['person'])])

                        elif field == 'object':
                            self.speaker.say('what\' is the subject?')
                            self.graph_module.exchange('System', 'what is the object?')
                            mail['object'] = self.asr_module.transcribe_audio()
                            self.graph_module.exchange('User', mail['object'], None, [('person', mail['object'])])
                            # update graph

                        elif field == 'body':
                            self.speaker.say('what is the body of the email?')
                            self.graph_module.exchange('System', 'what is the body of the email?')
                            mail['body'] = self.asr_module.transcribe_audio(10)
                            self.graph_module.exchange('User', mail['body'], None, [('person', mail['body'])])
                            # update graph

                if self.ask_confirm('send'):
                    self.mail_module.dispatch_intent({'intent': intent, 'mail': mail})
                    self.speaker.say('mail sent')
                self.main_loop()
                return
            elif intent == 'list_email' or len(self.opened_mail) > 0:

                time = None
                object = None
                person = None
                for slot in slots:
                    if slot[0] == 'person':
                        person = slot[1]
                    elif slot[0] == 'object':
                        object = slot[1]
                    elif slot[0] == 'time':
                        time = slot[1]

                self.speaker.say(f'I m looking for emails {f"from {person}" if person is not None else ""} '
                f'{f"with object {object}" if object is not None else ""} '
                f'{f"received on {time}" if time is not None else ""}')

                self.graph_module.exchange('System',f'looking for emails {f"from {person}" if person is not None else ""} '
                                           f'{f"with object {object}" if object is not None else ""} '
                                           f'{f"received on {time}" if time is not None else ""}')

                # update graph

                self.opened_mail = self.mail_module.get_email(object, time, person)
                self.speaker.say(f"there are {len(self.opened_mail)} new emails"
                                 f"{f'da {person}' if person is not None else ''} "
                                 f"{f'in data {time}' if time is not None else ''} "
                                 f"{f'with object {object}' if object is not None else ''}")

                self.graph_module.exchange('System', f"there are {len(self.opened_mail)} new emails"
                                                     f"{f'da {person}' if person is not None else ''} "
                                                     f"{f'in data {time}' if time is not None else ''} "
                                                     f"{f'with object {object}' if object is not None else ''}")
                self.main_loop()
                return
            elif 'exit' in text:
                self.speaker.say('Bye')
                return
            elif 'help' in text:
                self.speaker.say('possible operations')
                self.graph_module.exchange('System', 'possible operations')
                self.main_loop()
                return
            else:
                self.speaker.say('I didnt understand')
                self.main_loop()
                return
        else: ###opened mail
            mail = self.opened_mail[0]
            self.speaker.say(f"mail from {mail['person']} with subject {mail['object']}, what do you want to do?")
            self.graph_module.exchange('System',
                                       f"mail from {mail['person']} with subject {mail['object']}, what do you want to do?")
            text = self.asr_module.transcribe_audio()

            if not text:
                self.main_loop()
                return

            intent, slots = self.understanding_module.process(text)

            if intent == 'read_email':
                self.graph_module.exchange('User', text, intent, None)
                self.speaker.say(f"{mail['body']}")
                self.graph_module.exchange('System', f"{mail['body']}")
                self.main_loop()
                return
            elif intent == 'delete_email':
                self.graph_module.exchange('User', text, intent, None)

                if self.ask_confirm('delete email'):
                    del self.opened_mail[0]
                    self.mail_module.dispatch_intent({'intent': intent, 'mail': mail})
                    self.speaker.say('email deleted')
                self.main_loop()
                return

            elif intent == 'forward_email':
                new_mail = {'body': mail['body'], 'object': f"fwd:{mail['object']}", 'person': None,
                                'time': {'day': 'today', 'month': 'today'}}
                for slot in slots:
                    if slot[0] == 'person':
                        new_mail['person'] = slot[1]
                if new_mail['person'] is None:
                    self.speaker.say('who should the email be forwarded to?')
                    self.graph_module.exchange('System', 'who should the email be forwarded to?')
                    new_mail['person'] = self.asr_module.transcribe_audio()
                    print("person:", new_mail['person'])
                    if not new_mail['person']:
                        self.main_loop()
                        return
                    self.graph_module.exchange('User', new_mail['person'], None, new_mail['person'])

                self.graph_module.exchange('User', text, intent, [('person', new_mail['person'])])

                if self.ask_confirm('submit'):
                    self.mail_module.dispatch_intent({'intent': intent, 'mail': new_mail})
                    self.speaker.say('forwarded email')
                self.main_loop()
                return

            elif intent == 'reply_email':
                new_mail = {'body': None, 'object': f're:{mail["object"]}', 'person': mail['person']}
                self.graph_module.exchange('User', text, intent, None)
                self.speaker.say('what is the body of the email?')
                self.graph_module.exchange('System', 'what is the body of the email?')
                new_mail['body'] = self.asr_module.transcribe_audio(10)

                self.graph_module.exchange('User', text, intent,
                               [('person', mail['person']), ('object', mail['object'])])

                if self.ask_confirm('answer'):
                    self.mail_module.dispatch_intent({'intent': intent, 'mail': new_mail})
                    self.speaker.say('answer sent')
                self.main_loop()
                return
            elif intent == 'close_email':
                self.graph_module.exchange('User', text, intent, None)
                self.graph_module.exchange('User', intent)
                if len(self.opened_mail) > 0:
                    del self.opened_mail[0]
                self.main_loop()
                return
            elif 'exit' in text:
                self.graph_module.exchange('User', intent)
                self.speaker.say('hello!')
                return
            else:
                self.graph_module.exchange('User', intent)
                self.speaker.say('I didnt understand')
                self.main_loop()
                return
    def ask_confirm(self, operation):
        self.speaker.say(f'are you sure you want {operation}?')
        t = self.asr_module.transcribe_audio(3)
        if not t:
            self.main_loop()
            return
        while 'yes' not in t and 'no' not in t and 'ok' not in t and 'sure' not in t:
            self.speaker.say(f'I dont understand, are you sure you want{operation}?')
            t = self.asr_module.transcribe_audio(3)
            if not t:
                self.main_loop()
                return
        if 'yes' in t or 'ok' in t or 'sure' in t:
            return True
        return False

print("running..")
# %%
app = App()

# %%
app.main_loop()
