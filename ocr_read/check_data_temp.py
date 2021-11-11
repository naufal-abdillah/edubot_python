import pickle

with open('raw_data_MTK J+S Komposisi dan Invers.txt', 'rb') as f:
    mynewlist = pickle.load(f)
print(mynewlist)

with open('raw_data_MTK J+S Komposisi dan Invers_classes.txt', 'rb') as f:
    mynewlist_classes = pickle.load(f)
print(mynewlist_classes)