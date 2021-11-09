# edubot_python
This repository contains 3 python programs:

*   predict_class.py
*   ocr_read.py
*   train.py

## predict_class.py
This program gives an output of prediction class with an input of questions string list saved with pickle library as .txt file. the output will be predictions groups containing lists of confidence whether each question belongs to each class.

Here is each chaptor to class representation
```
MTK S+J Fungsi Kuadrat = 1
MTK J+S Komposisi dan Invers = 2
MTK S+J Matriks = 3
MTK S+J Komposisi Invers = 4
MTK S+J Eksponen dan Logaritma = 5
MTK S+J Peluang = 6
MTK S+J Statistik = 7
```
## ocr_read.py
This program reads image inputs and scan them with keras_ocr. the scanned output will be converted into strings and then saved into .txt file with pickle to be able to be loaded into the model in predict_class.py program.

## train.py
this program process dataset and use them to train the selected model. the program load a machine learning model with .h5 format. The dataset used to train the model should be a python list saved with pickle. the required files are:
*   train_data.txt
*   train_label.txt
*   val_data.txt
*   val_label.txt

data files should be a list of question strings and the label files should be a list of each questions' class.
