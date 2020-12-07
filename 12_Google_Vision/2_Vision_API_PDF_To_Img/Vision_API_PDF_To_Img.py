import os
import io
import glob
from google.cloud import vision
from pdf2image import convert_from_path


TEMPORARY_DIR = 'temp/'
PDF_FILE = "roger-that/Form.pdf"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'serviceAccountKey.json'
client = vision.ImageAnnotatorClient()


def convert_to_jpeg(pdf_file):
    if not os.path.exists(TEMPORARY_DIR):
        os.makedirs(TEMPORARY_DIR)
    else:
        files = glob.glob(f'{TEMPORARY_DIR}/*')
        for file in files:
            os.remove(file)

    pdf_pages = convert_from_path(pdf_file, 300)
    counter = 1
    for page in pdf_pages:
        img_file = f'{TEMPORARY_DIR}converted_{str(counter)}.jpeg'
        counter += 1
        page.save(img_file, "JPEG")


def extract_text():
    convert_to_jpeg(PDF_FILE)
    files = glob.glob(f'{TEMPORARY_DIR}/*')
    for file in files:
        with io.open(file, 'rb') as img_file:
            content = img_file.read()

        image = vision.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations

        for text in texts:
            print('\n"{}"'.format(text.description))

            vertices = (['({},{})'.format(vertex.x, vertex.y)
                         for vertex in text.bounding_poly.vertices])

            print('bounds: {}'.format(','.join(vertices)))

        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))


extract_text()
