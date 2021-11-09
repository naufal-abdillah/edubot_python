import tensorflow as tf
import os
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

# from tensorflow.keras.preprocessing.text import Tokenizer
def remove_digit(sentences):
  removed = sentences
  for index, text in enumerate(removed):
    new_text = ''.join([i for i in text if not i.isdigit()])
    removed[index] = new_text
  return removed

# Tokenizer
cwd = os.getcwd()
with open(os.path.join(cwd,'tokenizer.pickle'), 'rb') as handle:
  tokenizer = pickle.load(handle)

vocab = 1000
max_len = 48

def vectorize_sequences(sequences, dimension=vocab):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results

def string_to_vec(test_sentences, max_len = max_len):
  test_sentences = remove_digit(test_sentences)
  test_sequences = tokenizer.texts_to_sequences(test_sentences)
  test_padded = pad_sequences(test_sequences, maxlen=max_len)
  test_vectorized = vectorize_sequences(test_padded)
  return test_vectorized

#loading questions.txt
with open(os.path.join(cwd,'questions.txt'), 'rb') as handle:
  questions = pickle.load(handle)

to_predict = string_to_vec(questions)
model = tf.keras.models.load_model(os.path.join(cwd,'my_model.h5'))
predictions = model.predict(to_predict)
print(np.argmax(predictions))

