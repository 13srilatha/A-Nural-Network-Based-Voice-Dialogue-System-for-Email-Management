﻿import sys
from datasets import load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2FeatureExtractor, Wav2Vec2CTCTokenizer
from transformers import Wav2Vec2Processor, TrainingArguments, IntervalStrategy, Trainer
from lib import *


# %% INITIALIZE PROCESSOR


processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")


data_collator = DataCollatorCTCWithPadding(processor=processor, padding=True)

# %% PROCESS DATASET
# se hai già il file:
train_data, eval_data, test_data = load_dataset(processor)

# %% DEFINE METRICS

wer_metric = load_metric("wer")


def compute_metrics(pred):
    pred_logits = pred.predictions
    pred_ids = np.argmax(pred_logits, axis=-1)

    pred.label_ids[pred.label_ids == -100] = processor.tokenizer.pad_token_id

    pred_str = processor.batch_decode(pred_ids)
    # we do not want to group tokens when computing the metrics
    label_str = processor.batch_decode(pred.label_ids, group_tokens=False)

    wer = wer_metric.compute(predictions=pred_str, references=label_str)

    return {"wer": wer}


# %% LOAD PRETRAINED MODEL

model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h", vocab_size=40, ignore_mismatched_sizes=True)

model.freeze_feature_encoder()

# %% SET TRAINING PARAMETERS


training_args = TrainingArguments(
    output_dir='models/wav2vec2',
    group_by_length=True,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=1,
    evaluation_strategy=IntervalStrategy.EPOCH,
    num_train_epochs=1,
    gradient_checkpointing=True,
    fp16=False,
    save_steps=400,
    eval_steps=400,
    logging_steps=400,
    learning_rate=3e-4,
    warmup_steps=500,
    save_total_limit=2,
    push_to_hub=False,
)

# %% BUILD TRAINER

trainer = Trainer(
    model=model,
    data_collator=data_collator,
    args=training_args,
    compute_metrics=compute_metrics,
    train_dataset=train_data,
    eval_dataset=eval_data,
    tokenizer=processor.feature_extractor
)

# %% TRAIN


trainer.train()

model.save_pretrained("models/wav2vec2")
