import os
import sys
import PyPDF2

watermark = sys.argv[1]
files = sys.argv[2:]
output_dir = './pdf/watermarked_pdf/'

def pdf_watermarker(watermark, files):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    converted_watermark_file = PyPDF2.PdfFileReader(open(watermark, 'rb'))
    watermark_page = converted_watermark_file.getPage(0)

    for file in files:
        count = 1
        writer = PyPDF2.PdfFileWriter()
        read_single_file = PyPDF2.PdfFileReader(open(file, 'rb'))
        for page in range(read_single_file.numPages):
            new_page = read_single_file.getPage(page)
            new_page.mergePage(watermark_page)
            writer.addPage(new_page)

        while (True):
            output_filename = f'{output_dir}merged_file_{count}.pdf'
            if not os.path.exists(output_filename):
                writer.write(open(output_filename, 'wb'))
                break
            else:
                count += 1

pdf_watermarker(watermark, files)