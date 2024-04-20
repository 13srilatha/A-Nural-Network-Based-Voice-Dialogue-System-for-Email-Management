# A Nural Network-Based Voice Dialogue System for Email Management
 
A voice email manager ... with Neural Networks. It use a wav2vec2 + LM for asr, google cloud tts for voice and bert for understanding ( intent classification and token classification ). The system is trained with syntetic data. It use rdf for dialogue state tracking and smtp/pop3 to comunicating with email server..

Steps to build the AI pipeline:
to train your own system first create a python 3.8 virtual enviroment and install the requirements then follow these steps:

Generate training data
create python 3.8 virtualenv with requirements

write a file in data/names.txt with some rows in the format:

name,surname

with random names and surnames. you must have also a google api tts auth key saved as data/tts_auth_key.json

run generate_dataset notebook. this will create a data/dataset.csv file and a data/audio folder.

now you can safely delete data/names.txt

ASR fine tuning:
run fine tuning notebook (notebook/asr/train_asr.py). this will get you a models/wav2vec2 folder with torch model
you can now safely delete data/audio and data/hfdata folders
LM generation:
from command line cd into lib and run get_lm_corpus.sh this will get you 200 mb of data from paisa italian corpus in data/lm/corpus.txt
cd into lib/lm and run get_kenlm.sh to get kenlm executables
run notebooks/asr/build_lm.sh this will generate a lm model in models/lm/lm.arpa
run build_asr_with_lm notebook to generate a model in models/wav2vec2LM
if you run notebooks/asr/infer_asr you get the result of asr with lm. you can safely delete models/lm and models/wav2vec2. you can also safely delete data/hfdata folder
Tokens and Intent Classification
run notebooks/bert/train_token_clf.py notebook to train token classifier. this will get you a model/bert4token and model/berttokenizer folders with pytorch models
run notebooks/bert/train_seq_clf.py notebook to train intent classificator. this will get you a model/bert4sequence folder with the pytorch model
now you can safely delete data/dataset.csv
Email Module
buil a email.conf file in the following format:

smtp_server:smtp_port

pop3_server:pop3_port

email:password

build a contacts.txt with evrey row in the format (one for each contact in your library)

name surname:email

Start the app
execute main.py
