import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
# from model import predict_sentiment

import re
CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

def preprocessed(document):
  from string import punctuation
  punctuation = punctuation + '\n'
  stopwords = list(STOP_WORDS)
  return [word for word in document if word.text.lower() not in stopwords and word.text.lower() not in punctuation]

def get_normalised_word_frequencies(document):
  word_frequencies = {}
  for word in preprocessed(document):
      word_frequencies[word.text] = 1 if word.text not in word_frequencies else word_frequencies[word.text] + 1
  max_frequency = max(word_frequencies.values())
  for word in word_frequencies:
    word_frequencies[word] /= max_frequency
  return word_frequencies

def extracted_summary(text, percentage_reduced = 0.1, length = 0):
  nlp = spacy.load('en_core_web_sm')
  text = cleanhtml(text)
  doc = nlp(text)
  tokens = [token.text for token in doc]
  word_frequencies = get_normalised_word_frequencies(doc)
  sentence_scores = {sent: sum([word_frequencies[word.text.lower()] 
                                for word in sent if word.text.lower() in word_frequencies]) 
                                for sent in list(doc.sents)}
  select_length = length if length != 0 else int(len(list(doc.sents)) * percentage_reduced)
  summary = nlargest(select_length, sentence_scores, key = sentence_scores.get) 
  return ' '.join([word.text for word in summary])

# def sentiment(text: str) -> str:
#     return predict_sentiment(text)