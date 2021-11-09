import keras_ocr
import os
import pickle
pipeline = keras_ocr.pipeline.Pipeline()

cwd = os.getcwd()

images = []
for dir in os.listdir(cwd):
    if dir.endswith(".png") or dir.endswith(".jpg"):
        images.append(os.path.join(cwd,dir))
prediction_groups = pipeline.recognize(images)


#Prediction Groups to String
def pred_to_string(prediction_groups):
  results = []
  for prediction in prediction_groups:
    temp = []
    for text in prediction:
      temp.append(text[0])
    results.append(' '.join(temp))
  return results

pred_strings = pred_to_string(prediction_groups)
print(pred_strings)

#Saving ocr scanned questions strings list as txt
with open(os.path.join(cwd,"questions.txt"), "wb") as fp:
  pickle.dump(pred_strings, fp)
