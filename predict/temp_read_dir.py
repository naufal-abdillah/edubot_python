from ocr_read import ocr_read
datadir = "E:\Magang Glints\EduBot\edubot_python\predict\predicted_images"
texts = ocr_read.read_image_dir(datadir,False)
print(texts)