import sentencepiece as spm
import numpy as np

# train spm tokenizer with vacabulary size 10000
spm.SentencePieceTrainer.train(input='classical_articals.txt',model_prefix='classical_tokenizer',vocab_size=10000)

# load trained tokenizer model
sp = spm.SentencePieceProcessor(model_file='classical_tokenizer.model')
with open('classical_articals.txt','r',encoding='utf-8') as f:
    data = f.read()

n = len(data)
train_data = data[:int(n*0.9)]
val_data = data[int(n*0.9):]

train_ids = sp.encode_as_ids(train_data)
val_ids = sp.encode_as_ids(val_data)

print(f"train has {len(train_ids)} tokens")
print(f"val has {len(val_ids)} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile('train.bin')
val_ids.tofile('val.bin')
