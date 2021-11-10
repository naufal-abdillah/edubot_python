import ocr_read
import os

cwd = os.getcwd()
os.chdir("..")
datadir = os.path.join(os.getcwd(),"dataset\\temp")

ocr_read.read_image_data(datadir, cwd, "temp")

# print(datadir)2