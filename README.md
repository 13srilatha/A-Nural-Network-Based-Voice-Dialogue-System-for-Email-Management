# A Nural Network-Based Voice Dialogue System for Email Management
 
A voice email manager ... with Neural Networks. It use a wav2vec2 + LM for asr, google cloud tts for voice and bert for understanding ( intent classification and token classification ). The system is trained with syntetic data. It use rdf for dialogue state tracking and smtp/pop3 to comunicating with email server..

**Steps to build the AI pipeline:**
to train your own system first create a python 3.8 virtual enviroment and install the requirements then follow these steps:

**Generate training data:**
1. create python 3.8 virtualenv with requirements

2. write a file in data/names.txt with some rows in the format:

name,surname

with random names and surnames. you must have also a google api tts auth key saved as data/tts_auth_key.json

3. run generate_dataset notebook. this will create a data/dataset.csv file and a data/audio folder.

now you can safely delete data/names.txt

**ASR fine tuning:**
1. run fine tuning notebook (notebook/asr/train_asr.py). this will get you a models/wav2vec2 folder with torch model
you can now safely delete data/audio and data/hfdata folders
LM generation:
1. from command line cd into lib and run get_lm_corpus.sh this will get you 200 mb of data from paisa italian corpus in data/lm/corpus.txt
cd into lib/lm and run get_kenlm.sh to get kenlm executables
2. run notebooks/asr/build_lm.sh this will generate a lm model in models/lm/lm.arpa
3. run build_asr_with_lm notebook to generate a model in models/wav2vec2LM
4. if you run notebooks/asr/infer_asr you get the result of asr with lm. you can safely delete models/lm and models/wav2vec2. you can also safely delete data/hfdata folder
Tokens and Intent Classification
5. run notebooks/bert/train_token_clf.py notebook to train token classifier. this will get you a model/bert4token and model/berttokenizer folders with pytorch models
6. run notebooks/bert/train_seq_clf.py notebook to train intent classificator. this will get you a model/bert4sequence folder with the pytorch model
now you can safely delete data/dataset.csv

**Email Module:**
buil a email.conf file in the following format:

1. smtp_server:smtp_port

2. pop3_server:pop3_port

3. email:password

4. build a contacts.txt with evrey row in the format (one for each contact in your library)

5. name surname:email

 **Start the app:**
execute main.py
