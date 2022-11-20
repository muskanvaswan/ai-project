import pandas as pd
import matplotlib.pyplot as plt
import datasets  #(1.13.3)

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,Dense, Dropout, SpatialDropout1D
from tensorflow.keras.layers import Embedding

sentiments = ["positive", "negative", "nuetral"]
dataset = datasets.load_dataset("cnn_dailymail", '3.0.0')
df = pd.DataFrame(list(dataset['train'])).rename(columns={"article":"text", 
      "highlights":"y"})[["text","y"]].head(10000)

SAMPLES = 20
df_train = df.iloc[SAMPLES + 1: 4 * SAMPLES]
texts = df_train["y"]
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(texts)
vocab_size = len(tokenizer.word_index) + 1
encoded_docs = tokenizer.texts_to_sequences(texts)
padded_sequence = pad_sequences(encoded_docs, maxlen=200)

embedding_vector_length = 32
model = Sequential() 
model.add(Embedding(vocab_size, embedding_vector_length, input_length=200) )
model.add(SpatialDropout1D(0.25))
model.add(LSTM(50, dropout=0.5, recurrent_dropout=0.5))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid')) 
model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy'])  

def predict_sentiment(text):
    tw = tokenizer.texts_to_sequences([text])
    tw = pad_sequences(tw,maxlen=200)
    prediction = int(model.predict(tw).round().item())
    return sentiments[prediction]