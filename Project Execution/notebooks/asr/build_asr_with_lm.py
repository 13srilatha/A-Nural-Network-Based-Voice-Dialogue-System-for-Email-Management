import librosa
import torch
from pyctcdecode import build_ctcdecoder
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor, Wav2Vec2ProcessorWithLM

# %% INITIALIZE MODEL

# repo_name = 'maher13/English_ASR'
repo_name = 'jonatasgrosman/wav2vec2-large-xlsr-53-english'
model = Wav2Vec2ForCTC.from_pretrained(repo_name)
processor = Wav2Vec2Processor.from_pretrained(repo_name)

# %% BUILD LM PROCESSOR

vocab_dict = processor.tokenizer.get_vocab()
sorted_vocab_dict = {k: v for k, v in sorted(vocab_dict.items(), key=lambda item: item[1])}

print(vocab_dict)

decoder = build_ctcdecoder(
    labels=list(sorted_vocab_dict.keys()),
    kenlm_model_path= r"/mnt/c/Users/srila/OneDrive/Desktop/project2/blind-mailai/notebooks/asr/models/lm/lm.arpa",
)

processor_with_lm = Wav2Vec2ProcessorWithLM(feature_extractor=processor.feature_extractor,
                                            tokenizer=processor.tokenizer,
                                            decoder=decoder)


#%% SAVE MODEL

model.save_pretrained("models/wav2vec2LM")
processor_with_lm.save_pretrained('models/wav2vec2LM')



