import ocr_read
import os

cwd = os.getcwd()
os.chdir("..")
datadir = os.path.join(os.getcwd(),"dataset\\data_augmented")

ocr_read.read_image_data(datadir, cwd, "augmented_data")

# print(datadir)2