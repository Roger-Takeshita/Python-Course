import os
import sys
import PyPDF2

files = sys.argv[1:]

def pdf_combiner(files):
    output_path = './pdf/merged_pdfs/'

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    merger = PyPDF2.PdfFileMerger()

    for file in files:
        merger.append(file)

    merger.write(f'{output_path}combined_pdf.pdf')

pdf_combiner(files)
