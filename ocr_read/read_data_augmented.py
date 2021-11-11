import ocr_read
import os

cwd = os.getcwd()
os.chdir("..")
datadir = os.path.join(os.getcwd(),"dataset\\data_augmented\\MTK J+S Komposisi dan Invers")

# ocr_read.read_image_data(datadir, cwd, "raw_data")

ocr_read.read_image_dir(datadir, cwd, "aug_data_MTK J+S Komposisi dan Invers")
# print(datadir)2