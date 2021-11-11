import tensorflow as tf
import os
import pickle
import numpy as np
from ocr_read import ocr_read
from tensorflow.keras.preprocessing.sequence import pad_sequences

def remove_digit(sentences):
  removed = sentences
  for index, text in enumerate(removed):
    new_text = ''.join([i for i in text if not i.isdigit()])
    removed[index] = new_text
  return removed

# Load Tokenizer
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



def pred_to_name(pred):
    names = [
        "",
        "MTK S+J Fungsi Kuadrat" ,
        "MTK J+S Komposisi dan Invers",
        "MTK S+J Matriks" ,
        "MTK S+J Komposisi Invers",
        "MTK S+J Eksponen dan Logaritma",
        "MTK S+J Peluang",
        "MTK S+J Statistik"
    ]
    return names[pred]

def predictions_to_classnames(predictions):
    classnames = []
    for pred in predictions:
        temp = pred_to_name(np.argmax(pred))
        classnames.append(temp)
    return classnames

images_path = os.path.join(os.getcwd(),"predicted_images")
texts = ocr_read.read_image_dir(images_path,False)

to_predict = string_to_vec(texts)
model = tf.keras.models.load_model(os.path.join(cwd,'my_model.h5'))
predictions = model.predict(to_predict)

classnames = predictions_to_classnames(predictions)
print(classnames)

