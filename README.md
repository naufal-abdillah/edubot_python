# edubot_python
edubout_python classifies a math questions into the chapter name. It can process multiple inputs in the form of .png and .jpg images placed in a selected folder. 

edubot_python includes 2 main processess. the first process that takes place is to scan the images in the "predicted_images" folder into text with [keras_ocr](https://keras-ocr.readthedocs.io/en/latest/). The second main process is to classify the text string list to the classses using a machine learning text processing model. 

For more info check wiki.
# Prerequisites
The required libraries are following:
* os
* numpy
* tensorflow
* pickle
* cv2
* keras-ocr

to instal requirements run the following code:
```
pip install -r requirements.txt

```
and then install keras-ocr with following code:
```
# To install from master
pip install git+https://github.com/faustomorales/keras-ocr.git#egg=keras-ocr

# To install from PyPi
pip install keras-ocr

```
# How to Use the Classifier
The classifier is located in the "predict" folder as "classify_images.py". Put the images in "predict/predicted_images", and then run the classify_images.py program:
```
python classify_images.py

```
# How it works
* The classify_images.py will the program will call ocr_read.py located in ocr_read folder 
* ocr_read.py will iterate through predict/predicted_images and list the image files 
* the listed image files then scanned with keras_ocr giving prediction groups output
* the prediction groups then converted into strings and then given back to classify_images.py
* the string then converted into the required format for the text classifier
* classify_images loads the text classifier model located in the same folder, then classify the scanned strings
*  classify_images converts prediction ouput into the chapter names and print them

# Inputs
The input files are image files located in predict/predicted_images

![predicted_images](https://raw.githubusercontent.com/naufal-abdillah/edubot_python/master/examples/1.jpg)

here are the math question screenshots we use as predicted images

![komposisi](https://raw.githubusercontent.com/naufal-abdillah/edubot_python/master/predict/predicted_images/to_predict_1.png) ![peluang](https://raw.githubusercontent.com/naufal-abdillah/edubot_python/master/predict/predicted_images/to_predict_2.png) 

# Output
The classify_images prints the chapters in the form of a list

![output list](https://raw.githubusercontent.com/naufal-abdillah/edubot_python/master/examples/2.jpg)

# Text Classifier Model
The model trained gives the accuracy >0.9 with the dataset we use. The dataset is located in the dataset folder

![acc](https://raw.githubusercontent.com/naufal-abdillah/edubot_python/master/examples/3.png)
![loss](https://github.com/naufal-abdillah/edubot_python/blob/master/examples/4.png?raw=true)

You can see the training process of the text classifier in this [google colab notebook](https://colab.research.google.com/drive/1xQugWAoWPtqbY19pCTFd8I725TQAmJB_?usp=sharing)
