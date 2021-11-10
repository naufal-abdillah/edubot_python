import keras_ocr
import os
import pickle

def save_list(list_tosave, dest, filename):
    with open(os.path.join(dest, filename), "wb") as fp:
        pickle.dump(list_tosave, fp)

#Prediction Groups to String
def pred_to_string(prediction_groups):
  results = []
  for prediction in prediction_groups:
    temp = []
    for text in prediction:
      temp.append(text[0])
    results.append(' '.join(temp))
  return results

def iterate_imagepath(directory):
  images = []
  labels = []
  #iterate through dataset
  for dir in os.listdir(directory):
    nextdir = os.path.join(directory, dir)
    # is current iteration directory
    if os.path.isdir(nextdir):
      for filename in os.listdir(nextdir):
        if filename.endswith(".png") or filename.endswith(".jpg"):
          file_path = os.path.join(nextdir, filename)
          images.append(file_path)
          labels.append(dir)
          continue
        else:
            continue
  return images, labels

def read_image_data_wlabel(datadir, dest, filename):
    pipeline = keras_ocr.pipeline.Pipeline()
    images, labels = iterate_imagepath(datadir)
    prediction_groups = pipeline.recognize(images)
    pred_strings = pred_to_string(prediction_groups)
    #saving prediction strings
    save_list(pred_strings, dest, filename)
    #saving class labels
    save_list(labels, dest, filename+"_classes")


# cwd = os.getcwd()
#
# images = []
# for dir in os.listdir(cwd):
#     if dir.endswith(".png") or dir.endswith(".jpg"):
#         images.append(os.path.join(cwd,dir))
# prediction_groups = pipeline.recognize(images)
#
#
#
#
# pred_strings = pred_to_string(prediction_groups)

#Saving ocr scanned questions strings list as txt
# with open(os.path.join(cwd,"questions.txt"), "wb") as fp:
#   pickle.dump(pred_strings, fp)
