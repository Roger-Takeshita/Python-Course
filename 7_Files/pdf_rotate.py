import PyPDF2
import os
output_folder = './pdf/converted/'

with open('./pdf/dummy.pdf', 'rb') as my_file:
    #! Read the binary file
    reader = PyPDF2.PdfFileReader(my_file)

    #! Select the name
    filename = os.path.splitext(os.path.basename(my_file.name))

    #! Rotate a page
    selected_page = reader.getPage(0)
    selected_page.rotateClockwise(180)

    #! Print the number of pages
    print(reader.numPages)

    #! Save (write) a new file
    #+ first we instantiate the .PdfFileWriter()
    #+ create the file in mode 'wb' (write binary)
    writer = PyPDF2.PdfFileWriter()
    #+ write to the pdf
    writer.addPage(selected_page)

    #+ check if folder exists, if not create one
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    #+ save the file
    with open(f'{output_folder}{filename[0]}_converted.pdf', 'wb') as converted_file:
        writer.write(converted_file)