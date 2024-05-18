# github.com/tavukcobani
import os
from PIL import Image

def resize_images(input_folder, output_folder, size, quality=85):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    count = 1
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
            img = Image.open(os.path.join(input_folder, filename))
            img.thumbnail(size, Image.LANCZOS)
            
            ext = os.path.splitext(filename)[1]
            new_filename = f"image_{count}{ext}"
            output_path = os.path.join(output_folder, new_filename)
            
            if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
                img.save(output_path, quality=quality, optimize=True) 
            else:
                img.save(output_path)
            
            print(f"Resized {filename} -> {new_filename}")
            count += 1

input_folder = './input/'
output_folder = './output/'
size = (800, 800)

resize_images(input_folder, output_folder, size)
