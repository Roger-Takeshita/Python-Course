from pdf2image import convert_from_path
import os

output_dir = "images/"


def convert_file(file, output):
    if not os.path.exists(output):
        os.makedirs(output)

    pages = convert_from_path(file, 300)
    counter = 1
    for page in pages:
        my_file = f'{output}converted_{str(counter)}.png'
        counter += 1
        page.save(my_file, "PNG")


file = "pip_pdf2image.pdf"
convert_file(file, output_dir)
