from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import numpy as np
import cv2

BATCH_SIZE = 100
IMG_SHAPE  = 1000 # Our training data consists of images with width of 150 pixels and height of 150 pixels

os.chdir("..")
cwd = os.getcwd()
imagedir = os.path.join(cwd,"data_raw")
dest = os.path.join(cwd,"data_augmented")

datagen = ImageDataGenerator(
      rescale=1./255,
      rotation_range=40,
      width_shift_range=0.1,
      height_shift_range=0.1,
      shear_range=0.1,
      zoom_range=0.1,
      fill_mode='nearest')

import os

#iterate through dataset
for dir in os.listdir(imagedir):
  nextdir = os.path.join(imagedir, dir)

  # check if current iteration directory
  if os.path.isdir(nextdir):

    # augmented image class folder
    save_img_dir = os.path.join(dest, dir)

    # Iterate through class directory
    for filename in os.listdir(nextdir):
      if filename.endswith(".png") or filename.endswith(".jpg"):
        image_path = os.path.join(nextdir, filename)
        image = np.expand_dims(cv2.imread(image_path), 0)
        for x, val in zip(datagen.flow(image,                    #image we chose
                save_to_dir=save_img_dir,     #this is where we figure out where to save
                save_prefix='aug',        # it will save the images as 'aug_0912' some number for every new augmented image
                save_format='png'),range(10)) :     # here we define a range because we want 10 augmented images otherwise it will keep looping forever I think
          pass
        continue
      else:
          continue