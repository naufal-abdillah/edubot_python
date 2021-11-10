import pickle

with open('temp.txt', 'rb') as f:
    mynewlist = pickle.load(f)
print(mynewlist)

with open('temp_classes.txt', 'rb') as f:
    mynewlist_classes = pickle.load(f)
print(mynewlist_classes)