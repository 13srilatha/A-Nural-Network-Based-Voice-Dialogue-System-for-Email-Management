"""
-----------------
intent:

0 send_email
1 list_email
2 read_email
3 delete_email
4 reply_email
5 forward_email
6 close_email
------------------
entities:

O: outside
b-per: inzio slot persona
i-per: interno slot persona
b-obj: inizio slot oggetto
i-obj: interno slot oggetto
b-date: inizio slot data
i-date: interno slot data


O: outside
b-per: start of person slot
i-per: internal person slot
b-obj: start of object slot
i-obj: internal object slot
b-date: start of slot date
i-date: internal data slot
---------------------
"""

import random
import pandas as pd

import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f"{os.getcwd()}/data" + "/" + "tts_auth_key.json"
from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()


def generate_audio(text, index):
    voice_name = ['en-IN-Standard-A', 'en-IN-Standard-B', 'en-IN-Standard-C',
                  'en-IN-Standard-D', 'en-IN-Wavenet-A', 'en-IN-Wavenet-B',
                  'en-IN-Wavenet-C', 'en-IN-Wavenet-D'][random.randint(0, 7)]

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-IN", name=voice_name
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    if not os.path.isdir('data/audio'):
        os.mkdir('data/audio')
    # The response's audio_content is binary.
    with open(f"data/audio/{index}.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file')


def get_random_object():
    # conj = ' con ogetto'
    conj = ' with object'


    # ret_text = ['informazioni ricevimento', 'elezioni studentesche', 'Posticipo incontro',
    #             'Firme per la partecipazione al corso di informatica', 'Ritiro attestato',
    #             'Problema accesso sito universitario', 'Promemoria', 'info su prescrizione medica',
    #             'Assistenza tecnica', 'Reclamo e richiesta di assistenza', 'Candidatura spontanea',
    #             'comunicazione importante', 'ordine del giorno', 'richiesta modulo', 'consegna progetto',
    #             'conferma invito', 'attivazione profilo', 'convalida esame', 'abbonamento napoli calcio',
    #             'sottoscrizione abbonamento', 'scadenza consegna', 'rinnovo abbonamento netflix'][
    #     random.randint(0, 20)].lower()

    ret_text = ['reception information', 'student elections', 'Postpone meeting',
                'Signatures for participation in the computer course', 'Withdrawal of certificate',
                'Problem accessing university site', 'Reminder', 'info on medical prescription',
                'Technical assistance', 'Complaint and request for assistance', 'Spontaneous application',
                'important communication', 'agenda', 'form request', 'project delivery',
                'invitation confirmation', 'profile activation', 'exam validation', 'Naples football season ticket',
                'subscription subscription', 'delivery deadline', 'netflix subscription renewal'][
        random.randint(0, 21)].lower()

    ret_slot = ['O', 'O', 'B-OBJ'] + ['I-OBJ'] * (len(ret_text.split(' ')) - 1)

    return f"{conj} {ret_text}", ret_slot


with open('data/names.txt') as f:
    names = [name.replace('\n', '').replace(',', ' ') for name in f.readlines()]


def get_random_person(to=True):
    name = names[random.randint(0, len(names) - 1)]

    # conj = ['da', 'di', 'inviate da', 'con mittente'][random.randint(0, 3)]

    conj =  ['from', 'of', 'sent from', 'with sender'][random.randint(0, 3)]
    if to:
        # conj = ['a', 'per', 'con destinatario'][random.randint(0, 2)]
        conj = ['to', 'to', 'with recipient'][random.randint(0, 2)]

    return f" {conj} {name.lower()}", ['O'] * len(conj.split(' ')) + ['B-PER', 'I-PER']


def get_random_date():
    ret_text = ''
    ret_slots = []
    type = ['exact', 'relative', 'month'][random.randint(0, 2)]

    if type == 'exact':

        # conj = ['ricevute il', 'del', 'con data'][random.randint(0, 2)]
        conj = ['received on', 'on', 'with date'][random.randint(0, 2)]

        # day = ['primo', 'due', 'tre', 'quattro', 'cingue', 'sei', 'sette', 'otto', 'nove', 'dieci',
        #        'undici', 'dodici', 'tredici', 'quattordici', 'quindici', 'sedici', 'diciasette',
        #        'diciotto', 'diciannove', 'venti', 'ventuno', 'ventidue', 'ventitre', 'ventiquattro',
        #        'venticinque', 'ventisei', 'ventisette', 'ventotto', 'ventinove', 'trenta',
        #        'trentuno'][random.randint(0, 30)]

        day = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
               'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth',
               'eighteenth', 'nineteenth', 'twentieth', 'twenty-first', 'twenty-second', 'twenty-third', 'twenty-fourth',
               'twenty-fifth', 'twenty-sixth', 'twenty-seventh', 'twenty-eighth', 'twenty-ninth', 'thirtieth',
               'thirty-first'][random.randint(0, 30)]

        # month = ['gennaio', 'febbraio', 'marzo', 'aprile',
        #          'maggio', 'giugno', 'luglio', 'agosto',
        #          'settembre', 'ottobre', 'novembre', 'dicembre'][random.randint(0, 11)]

        month = ['January', 'February', 'March', 'April',
                 'May', 'June', 'July', 'August',
                 'September', 'October', 'November', 'December'][random.randint(0, 11)]


        ret_text = f"{conj} {day} {month}"
        ret_slots = ['O'] * len(conj.split(' ')) + ['B-DATE', 'I-DATE']
    elif type == 'relative':
        # ret_text, ret_slots = [('di questo mese', ['O', 'B-DATE', 'I-DATE']),
        #                        ('ricevute questo mese', ['O', 'B-DATE', 'I-DATE']),
        #                        ('del mese scorso', ['O', 'B-DATE', 'I-DATE']),
        #                        ('ricevute il mese scorso', ['O', 'O', 'B-DATE', 'I-DATE']),
        #                        ('di questa settimana', ['O', 'B-DATE', 'I-DATE']),
        #                        ('ricevute questa settimana', ['O', 'B-DATE', 'I-DATE']),
        #                        ('della settimana scorsa', ['O', 'B-DATE', 'I-DATE']),
        #                        ('ricevute la settimana scorsa', ['O', 'O', 'B-DATE', 'I-DATE']),
        #                        ('di oggi', ['O', 'B-DATE']),
        #                        ('ricevute oggi', ['O', 'B-DATE']),
        #                        ('di ieri', ['O', 'B-DATE']),
        #                        ('ricevute ieri', ['O', 'B-DATE'])][random.randint(0, 11)]

        ret_text, ret_slots = [('this month', ['O', 'B-DATE', 'I-DATE']),
                               ('received this month', ['O', 'B-DATE', 'I-DATE']),
                               ('last month', ['O', 'B-DATE', 'I-DATE']),
                               ('received last month', ['O', 'O', 'B-DATE', 'I-DATE']),
                               ('this week', ['O', 'B-DATE', 'I-DATE']),
                               ('received this week', ['O', 'B-DATE', 'I-DATE']),
                               ('last week', ['O', 'B-DATE', 'I-DATE']),
                               ('received last week', ['O', 'O', 'B-DATE', 'I-DATE']),
                               ('today', ['O', 'B-DATE']),
                               ('received today', ['O', 'B-DATE']),
                               ('yesterday', ['O', 'B-DATE']),
                               ('received yesterday', ['O', 'B-DATE'])][random.randint(0, 11)]


    elif type == 'month':
        # pref = ['ricevute a', 'di'][random.randint(0, 1)]
        # month = ['gennaio', 'febbraio', 'marzo', 'aprile',
        #          'maggio', 'giugno', 'luglio', 'agosto',
        #          'settembre', 'ottobre', 'novembre', 'dicembre'][random.randint(0, 11)]

        pref = ['received in', 'in'][random.randint(0, 1)]
        month = ['January', 'February', 'March', 'April',
                 'May', 'June', 'July', 'August',
                 'September', 'October', 'November', 'December'][random.randint(0, 11)]

        ret_text = f"{pref} {month}"
        ret_slots = ['O'] * len(pref.split(' ')) + ['B-DATE']
    return f" {ret_text}", ret_slots


def compose_sentence(intent):
    ret_text, ret_slots = "", None
    if intent == 0:

        if random.randint(1, 7) <= 4:
            # ret_text = ['potresti', 'vorresti', 'voglio', 'puoi'][random.randint(0, 1)] + \
            #            " " + ['inviare', 'mandare', 'spedire'][random.randint(0, 2)] + \
            #            " " + ['una mail', 'un messaggio'][random.randint(0, 1)]

            ret_text = ['could you', 'would you', 'I want to', 'can you'][random.randint(0, 1)] + \
                      " " + ['send', 'send', 'send'][random.randint(0, 2)] + \
                      " " + ['an email', 'a message'][random.randint(0, 1)]

            ret_slots = ['O', 'O', 'O', 'O']
        else:
            # ret_text = ['invia', 'manda', 'spedisci'][random.randint(0, 2)] + ' ' + \
            #            ['una mail', 'un messaggio'][random.randint(0, 1)]

            ret_text = ['send','send','send'][random.randint(0, 2)] + ' ' + \
                       ['an email', 'a message'][random.randint(0, 1)]

            ret_slots = ['O', 'O', 'O']

        additional_slots = [['obj'], ['obj', 'per'], ['per'], ['per', 'obj'], []][random.randint(0, 4)]

        text_to_add, slot_to_add = '', []
        for slot in additional_slots:
            if slot == 'obj':
                text_to_add, slot_to_add = get_random_object()
            elif slot == 'per':
                text_to_add, slot_to_add = get_random_person()
            ret_text += text_to_add
            ret_slots += slot_to_add

    elif intent == 1:

        n = random.randint(0, 2)

        if n == 0:
            # ret_text = ['potresti', 'vorresti'][random.randint(0, 1)] + ' ' + \
            #            ['cercarmi', 'leggermi', 'cercare', 'leggere'][random.randint(0, 3)] + ' ' + \
            #            ['le mail', 'i messaggi'][random.randint(0, 1)]

            ret_text = ['could you', 'would you'][random.randint(0, 1)] + ' ' + \
                       ['look for', 'read me', 'search', 'read'][random.randint(0, 3)] + ' ' + \
                       ['mails', 'messages'][random.randint(0, 1)]

            ret_slots = ['O', 'O', 'O', 'O']

        elif n == 1:
            # ret_text = ['vorrei', 'voglio'][random.randint(0, 1)] + ' ' + \
            #            ['cercare', 'leggere'][random.randint(0, 1)] + ' ' + \
            #            ['delle mail', 'dei messaggi', 'le mail', 'i messaggi'][random.randint(0, 1)]

            ret_text = ['I would like to', 'I want to'][random.randint(0, 1)] + ' ' + \
                       ['search', 'read', 'listen to'][random.randint(0, 1)] + ' ' + \
                       ['the emails', 'the messages', 'the emails', 'the messages'][random.randint(0, 1)]

            ret_slots = ['O', 'O', 'O', 'O']
        else:
            # ret_text = ['cerca', 'leggi', 'cerchi'][random.randint(0, 2)] + ' ' + \
            #            ['le mail', 'i messaggi'][random.randint(0, 1)]

            ret_text = ['search for', 'read', 'look for'][random.randint(0, 2)] + ' ' + \
                       ['mails', 'messages'][random.randint(0, 1)]

            ret_slots = ['O', 'O', 'O']

        slots = ['obj', 'per', 'date', 'no']

        additional_slots = [[t1, t2, t3] for t1 in slots for t2 in slots for t3 in slots
                            if (t1 != 'no' and t2 == 'no' and t3 == 'no') or
                            (t1 != 'no' and t2 != 'no' and t3 == 'no' and t1 != t2) or
                            (t1 != 'no' and t2 != 'no' and t3 != 'no' and t1 != t2 and t2 != t3 and t3 != t1)]

        additional_slots = additional_slots[random.randint(0, len(additional_slots) - 1)]
        for slot in additional_slots:
            text_to_add, slot_to_add = '', []
            if slot == 'obj':
                text_to_add, slot_to_add = get_random_object()
            elif slot == 'per':
                text_to_add, slot_to_add = get_random_person(to=False)
            elif slot == 'date':
                text_to_add, slot_to_add = get_random_date()

            ret_text += text_to_add
            ret_slots += slot_to_add

    elif intent == 2:

        n = random.randint(0, 2)
        if n == 0:
            # ret_text = ['potresti ', 'vorresti '][random.randint(0, 1)] + ' ' + \
            #            ['leggerla', 'leggermela'][random.randint(0, 1)]

            ret_text = ['could you ', 'would you '][random.randint(0, 1)] + ' ' + \
                       ['read it', 'read it to me'][random.randint(0, 1)]

        elif n == 1:
            # ret_text = ['vorrei', 'voglio'][random.randint(0, 1)] + ' ' + \
            #            ['leggerla', 'leggere la mail', 'leggere il messaggio'][random.randint(0, 2)]

            ret_text = ['I would like ti', 'I want to'][random.randint(0, 1)] + ' ' + \
                       ['read it', 'read the email', 'read the message'][random.randint(0, 2)]

        else:
            # ret_text = ['leggila', 'leggi', 'leggimela', 'leggimi la mail',
            #             'leggimi il messaggio', 'leggi la mail', 'leggi il messaggio'][random.randint(0, 4)]

            ret_text = ['read it', 'read', 'read it to me', 'read my email',
                        'read the message', 'read the email', 'read the message'][random.randint(0, 4)]

        ret_slots = ['O'] * len(ret_text.split(' '))
    elif intent == 3:

        if random.randint(0, 1) == 0:
            # ret_text = ['potresti', 'vorresti', 'vorrei', 'voglio'][random.randint(0, 3)] + ' ' + \
            #            ['cancellare la mail', 'cancellare il messaggio', 'eliminare la mail', 'cancellarla',
            #             'eliminare il messaggio', 'eliminarla'][random.randint(0, 5)]

            ret_text = ['could you', 'would you', 'I would like', 'I want to'][random.randint(0, 3)] + ' ' + \
                       ['delete the email', 'delete the message', 'delete the email', 'delete it',
                       'delete message', 'delete'][random.randint(0, 5)]

        else:
            # ret_text = ['cancella', 'cancella la mail', 'cancella il messaggio', 'elimina', 'elimina la mail',
            #             'elimina il messaggio', 'cancellala', 'eliminala'][random.randint(0, 7)]

            ret_text = ['delete', 'delete the email', 'delete the message', 'delete', 'delete the email',
                        'delete message', 'delete', 'delete'][random.randint(0, 7)]

        ret_slots = ['O'] * len(ret_text.split(' '))

    elif intent == 4:
        if random.randint(0, 1) == 0:

            # ret_text = ['potresti', 'vorresti', 'vorrei', 'voglio'][random.randint(0, 3)] + ' ' + \
            #            ['rispondere', 'rispondere alla mail', 'rispondere al messaggio', 'rispondergli'][
            #                random.randint(0, 3)]

            ret_text = ['could you', 'would you', 'I would like to', 'I want to'][random.randint(0, 3)] + ' ' + \
                       ['reply', 'reply to email', 'reply to message', 'reply to him'][random.randint(0, 3)]

        else:
            # ret_text = ['rispondi', 'rispondi alla mail', 'rispondi al messaggio', 'rispondigli'][random.randint(0, 3)]
            ret_text = ['reply', 'reply to email', 'reply to message', 'reply to him'][random.randint(0, 3)]

        ret_slots = ['O'] * len(ret_text.split(' '))

    elif intent == 5:
        if random.randint(0, 1) == 0:
            # ret_text = ['potresti', 'vorresti', 'vorrei', 'voglio'][random.randint(0, 3)] + ' ' + \
            #            ['inoltrare', 'inoltrare la mail', 'inoltrare il messaggio', 'inoltrarla'][random.randint(0, 3)]
            ret_text = ['could you', 'would you', 'I would like to', 'I want to'][random.randint(0, 3)] + ' ' + \
                       ['forward', 'forward the email', 'forward the message', 'forward it'][random.randint(0, 3)]

        else:
            # ret_text = ['inoltra', 'inoltra la mail', 'inoltra il messaggio', 'inoltrala'][random.randint(0, 3)]
            ret_text = ['forward', 'forward the email', 'forward the message', 'forward it'][random.randint(0, 3)]

        ret_slots = ['O'] * len(ret_text.split(' '))

        text_to_add, slot_to_add = get_random_person()
        ret_text += text_to_add
        ret_slots += slot_to_add
    elif intent == 6:
        if random.randint(0, 1) == 0:
            # ret_text = ['potresti', 'vorresti', 'vorrei', 'voglio'][random.randint(0, 3)] + ' ' + \
            #            ['chiudere', 'chiudere la mail', 'chiudere il messaggio', 'chiuderla', 'uscire',
            #             'uscire dalla mail', 'uscire dal messaggio'][random.randint(0, 6)]
            ret_text = ['could you', 'would you', 'I would like to', 'I want to'][random.randint(0, 3)] + ' ' + \
                       ['close', 'close email', 'close message', 'close it', 'exit',
                       'exit mail', 'exit message'][random.randint(0, 6)]

        else:
            # ret_text = ['chiudi', 'chiudila', 'chiudi la mail', 'chiudi il messaggio', 'esci dalla mail',
            #             'esci dal messaggio'][random.randint(0, 5)]
            ret_text = ['close', 'close it', 'close email', 'close message', 'exit email','exit message'][random.randint(0, 5)]


        ret_slots = ['O'] * len(ret_text.split(' '))

    if ret_text.count('con') > 1:
        tokens = ret_text.split(' ')
        found_first = False
        for i in range(len(tokens) - 1):
            # con=with ogget=object ed=and
            if tokens[i] == 'with' and not found_first:
                found_first = True
            elif tokens[i] == 'with' and tokens[i + 1] == 'object':
                tokens[i] = 'and'
            elif tokens[i] == 'with':
                tokens[i] = 'and'
        ret_text = ' '.join(tokens)

    return ret_text, ret_slots


# %% GENERATE TEXTUAL DATA AND LABELS

examples_for_intent = 150
text_array = []
slot_array = []
intent_array = []

for intent in range(7):
    for _ in range(examples_for_intent):
        text, slots = compose_sentence(intent)
        text_array.append(text)
        slot_array.append(slots)
        intent_array.append(intent)

res = pd.DataFrame.from_dict({'text': text_array, 'slots': slot_array, 'intent': intent_array})
res.to_csv('data/dataset.csv')


import time

df = pd.read_csv(r'data/dataset.csv')
c = 0
for i in df['text']:
    print(f'syntetization : {(c / len(df["text"]) * 100):.2f}%')
    generate_audio(i, c)
    c += 1