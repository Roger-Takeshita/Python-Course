import sys
import os
from PIL import Image

images_folder = sys.argv[1]
destination_folder = sys.argv[2]

print(images_folder, destination_folder)

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(images_folder):
    img = Image.open(f'{images_folder}{filename}')
    clean_name = os.path.splitext(filename)
    img.save(f'{destination_folder}{clean_name[0]}.png', 'png')