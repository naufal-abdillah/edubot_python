import tensorflow as tf
import pickle
import os

cwd = os.getcwd()

with open(os.path.join(cwd,"train_data.txt"), "rb") as fp:
  train_data = pickle.load(fp)
with open(os.path.join(cwd,"train_label.txt"), "rb") as fp:
  train_label = pickle.load(fp)
with open(os.path.join(cwd,"val_data.txt"), "rb") as fp:
  val_data = pickle.load(fp)
with open(os.path.join(cwd,"val_label.txt"), "rb") as fp:
  val_label = pickle.load(fp)
  
vocab = 1000
max_len = 48
def remove_digit(sentences):
  removed = sentences
  for index, text in enumerate(removed):
    new_text = ''.join([i for i in text if not i.isdigit()])
    removed[index] = new_text
  return removed

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

train_data = string_to_vec(train_data)
#train model with train data saved in txt by pickle

model = tf.keras.models.load_model(os.path.join(cwd,"my_model.h5"))
history = model.fit(train_data,
                    train_label,
                    epochs=20,
                    batch_size=512,
                    validation_data=(val_data, val_label))

model.save(os.path.join(cwd,'my_model.h5'))
