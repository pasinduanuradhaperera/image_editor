from PIL import Image,ImageEnhance,ImageFilter
import os
path = "./imgs"
pathout = "./edited"

for filename in os.listdir(path):
   img = Image.open(f"{path}/{filename}")
   edit = img.filter(ImageFilter.SHARPEN).convert().convert(-90)