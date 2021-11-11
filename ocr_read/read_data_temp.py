import ocr_read
import os

cwd = os.getcwd()
os.chdir("..")
datadir = os.path.join(os.getcwd(),"dataset\\temp")
image_path = "E:\\Magang Glints\\EduBot\\edubot_python\\dataset\\data_augmented\\MTK S+J Peluang\\aug_0_457.png"

# ocr_read.read_image_data(datadir, cwd, "temp")
image_text = ocr_read.read_image_path(image_path)
print(image_text)