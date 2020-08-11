<h1 id='summary'>Summary</h1>

-   [PIL - Image Processing](#imageprocessing)
    -   [Installation](#installpil)
    -   [PIL Basics](#pilbasics)
    -   [Image Converter (jpg to png](#imageconverter)
-   [PyPDF2 - PDF](#pypdf2)
    -   [Installation](#installpydf2)
    -   [PDF Basics](#pdfbasics)
    -   [Merge/Combine PDFs](#mergepdf)
    -   [Watermaker PDF](#watermakerpdf)
-   [smtplib - Email](#email)
    -   [SMTP Protocol](#smtpprotocol)
    -   [Using smtplib](#usingsmtplib)
        -   [String Template](#stringtemplate)
-   [hashlib - Hash Password](#hashlib)
    -   [Password Checker](#passwordchecker)

<h1 id='imageprocessing'>PIL - Image Processing</h1>

[Go Back to Summary](#summary)

-   [Pillow (PIL) - Official Docs](https://pillow.readthedocs.io/en/stable/about.html#goals)

<h2 id='installpil'>Installation</h2>

[Go Back to Summary](#summary)

-   install PIL

    ```Bash
      pip3 install Pillow
    ```

<h2 id='pilbasics'>PIL Basics</h2>

[Go Back to Summary](#summary)

-   Working with images

    ```Python
      from PIL import Image, ImageFilter

      img = Image.open('./yumi.png')

      print(img)
      print(img.mode)
      print(img.size)
      print(img.format)

      #! Blur
      filtered_img = img.filter(ImageFilter.BLUR)
      filtered_img.save('./images/converted/yumi_blur.png', 'png')

      #! Smooth
      filtered_img2 = img.filter(ImageFilter.SMOOTH)
      filtered_img2.save('./images/converted/yumi_smooth.png', 'png')

      #! Sharpen
      filtered_img3 = img.filter(ImageFilter.SHARPEN)
      filtered_img3.save('./images/converted/yumi_sharpen.png', 'png')

      #! Grey Scale
      filtered_img4 = img.convert('L') # 'L' = grey scale
      filtered_img4.save('./images/converted/yumi_grey_scale.png', 'png')

      #! Show Image
      # filtered_img4.show()

      #! Rotate
      rotated_img = filtered_img4.rotate(75)
      rotated_img.save('./images/converted/yumi_rotated.png', 'png')

      #! Resize
      resized_img = img.resize((300, 300))
      resized_img.save('./images/converted/yumi_300x300.png', 'png')

      #! Crop
      box = (100, 100, 400, 400)
      cropped_img = img.crop(box)
      cropped_img.save('./images/converted/yumi_cropped.png', 'png')

      #! Thumbnail
      img.thumbnail((150 ,150))
      img.save('./images/converted/yumi_thumbnail.png')
    ```

<h2 id='imageconverter'>Image Converter (jpg to png)</h2>

[Go Back to Summary](#summary)

-   To use the image converter, we first need to import the `sys` module to get the input from the user
-   We need to import `os` or `pathlib` (alternative)
    -   [os - Official Docs](https://docs.python.org/3/library/os.html)
    -   [pathlib - Official Docs](https://docs.python.org/3/library/pathlib.html)
-   To use run the code we need to give the images_folder and the destination folder, like so:
-   `python3 image_converter.py images/images_jpg/ images/images_png/`

    ```Python
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
    ```

<h1 id='pypdf2'>PyPDF2 - PDF</h1>

[Go Back to Summary](#summary)

-   To work with PDFs we are going to use `PyPDF2`
-   [PyPDF2 - Official Docs](https://pythonhosted.org/PyPDF2/)

<h2 id='installpydf2'>Installation</h2>

[Go Back to Summary](#summary)

-   Install `PyDF2`

    ```Bash
      pip3 install PyPDF2
    ```

<h2 id='pdfbasics'>PDF Basics</h2>

[Go Back to Summary](#summary)

-   `PdfFileReader(my_file)` - Read the PDF in binary format
    -   `rb` - Ready Binary
-   `.numPages`
-   `.getPage(0)` - Get the first page
-   `.rotateClockwise()` - Rotate a page, first we need to get page, then we can rotate
-   `.rotateCounterClockwise()` - Rotate a page, first we need to get page, then we can rotate
-   `.PdfFileWriter()` - Writer
-   `.addPage()` - Adds a new page
-   `.write()` - Save the modified file
-   `.PdfFileMerger()` - Combine multiple pdfs

    ```Python
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
    ```

<h2 id='mergepdf'>Merge/Combine PDFs</h2>

[Go Back to Summary](#summary)

-   Similar to write a PDF (`.PdfFileWriter()`) we have the merger (`PdfFileMerger()`)

    ```Bash
      python3 pdf_combiner.py pdf/dummy.pdf pdf/twopage.pdf pdf/wtr.pdf
    ```

    ```Python
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
    ```

<h2 id='watermakerpdf'>Watermaker PDF</h2>

[Go Back to Summary](#summary)

-   Watermaker PDF, where the first argument is the watermark then the rest are the files

    ```Bash
      python3 pdf_watermaker.py pdf/wtr.pdf pdf/dummy.pdf pdf/twopage.pdf
    ```

    ```Python
      import os
      import sys
      import PyPDF2

      watermark = sys.argv[1]
      files = sys.argv[2:]
      output_dir = './pdf/watermarked_pdf/'

      def pdf_watermarker(watermark, files):
          if not os.path.exists(output_dir):
              os.makedirs(output_dir)

          with open(watermark, 'rb') as watermark_file:
              converted_watermark_file = PyPDF2.PdfFileReader(watermark_file)
              watermark_page = converted_watermark_file.getPage(0)

              for file in files:
                  with open(file, 'rb') as single_file:
                      count = 1
                      writer = PyPDF2.PdfFileWriter()
                      read_single_file = PyPDF2.PdfFileReader(single_file)
                      for page in range(read_single_file.numPages):
                          new_page = read_single_file.getPage(page)
                          new_page.mergePage(watermark_page)
                          writer.addPage(new_page)

                      while (True):
                          output_filename = f'{output_dir}merged_file_{count}.pdf'
                          if not os.path.exists(output_filename):
                              with open(output_filename, 'wb') as new_file:
                                  writer.write(new_file)
                              break
                          else:
                              count += 1

      pdf_watermarker(watermark, files)
    ```

-   Little refactoring:

    ```Python
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
    ```

<h1 id='email'>smtplib - Email</h1>

[Go Back to Summary](#summary)

-   Python has a built-in email module called `smtplib`
-   [smtplib - Official Docs](https://docs.python.org/3/library/email.examples.html)

<h2 id='smtpprotocol'>SMTP Protocol</h2>

[Go Back to Summary](#summary)

-   **SMTP**, or **Simple Mail Transfer Protocol**, is a set of communication guidelines used by email servers to deliver emails to their clients. Your emails are just strings of text; **SMTP** helps servers and email clients categorize and organize the information you send. When you send an email, the sender, recipients, email body and title heading are separated into sections. **SMTP** separates the sections using code words.

-   **SMTP Usage**
    **SMTP** is used to send emails, so it only works for outgoing emails. To be able to send emails, you need to provide the correct SMTP server when you set up your email client. Unlike POP3 and IMAP, SMTP can't be used to retrieve and store emails. **SMTP** is also responsible for setting up communication between servers. The first server identifies itself and transmits the type of operation it will perform. The email is sent only after the second server authorizes the operation. SMTP is simple and reliable, but not very secure. Because it is text-based, **SMTP** is vulnerable to spoofing.

<h2 id='usingsmtplib'>Using smtplib</h2>

[Go Back to Summary](#summary)

-   Import the the library and `EmailMessage`

    ```Python
      import stmtplib
      from email.message import EmailMessage
    ```

-   Then create a new email object using `EmailMessage()`

    -   Add, who is this email from?
        -   `email['from'] = 'Your Name'`
    -   Add, who are we sending the email to
        -   `email['to'] = 'user_email@gmail.com'`
    -   Add the email's subject line
        -   `email['subject'] = 'It\'s your lucky day Yumi'`
    -   Add the content
        -   `email.set_content('Hi Yumi, you just won $1.000 and 2x bones')`

-   After setting up the the email object content, we need to send the email

    ```Python
      with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
          # ehlo, this is a part of the protocol of the smtp
          smtp.ehlo()
          # starts the encryption protocol
          smtp.starttls()
          # login to gmail acc with your credentials
          stmp.login('your_email@gmail.com', 'your_password')
          # send the email that we just created
          smtp.send_message(email)
          print('message sent')
    ```

    ```Python
      import smtplib
      from email.message import EmailMessage

      email = EmailMessage()
      email['From'] = 'Your Name'
      email['To'] = 'user_email@gmail.com'
      email['Subject'] = 'It\'s your lucky day Yumi'
      email.set_content('Hi Yumi, you just won $1.000 and 2x bones')

      with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
          # ehlo, this is a part of the protocol of the smtp
          smtp.ehlo()
          # starts the encryption protocol
          smtp.starttls()
          # login to gmail acc with your credentials
          smtp.login('your_email@gmail.com', 'your_password')
          # send the email that we just created
          smtp.send_message(email)
          print('message sent')
    ```

-   **ATTENTION** the name of the file has to be anything different from `email.py`

<h3 id='stringtemplate'>String Template</h3>

[Go Back to Summary](#summary)

-   `String Template` is a a built-in class (`class string.Template(template)`), just like template literals
    -   [string.Template - Official Docs](https://docs.python.org/3/library/string.html)
-   In this case we are going to read the `html` file, then we are going to substitute the variable `$name`
    -   to access the `html` file, we are going to use `pathlib`, we could also use `os`
    -   [pathlib vs os](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)
-   Then instead of sending a fixed text, we can substitute the `$name` with a dynamic name
    -   `html.substitute(name='Yumi')` or `html.substitute({'name': name})`
    -   the `email.set_content()` has a second parameter, that we can specify the format
        -   we can set the email content to be `html`, so the email will be formatted as `html`

*   in `email_send.html`

    -   Let's create a base `html` file

    ```HTML
      <!DOCTYPE html>
      <html lang="en">

      <head>
      </head>

      <body>
          $name just won 1.000,00 CAD and 2x bones
      </body>

      </html>
    ```

*   in `email_send.py`

    ```Python
      import smtplib
      from email.message import EmailMessage
      from string import Template
      from pathlib import Path

      name = 'Yumi'
      html = Template(Path('email_send.html').read_text())
      email = EmailMessage()
      email['From'] = 'Your Name'
      email['To'] = 'user_email@gmail.com'
      email['Subject'] = f'It\'s your lucky day {name}'
      email.set_content(html.substitute({'name': name}), 'html')

      with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
          smtp.ehlo()
          smtp.starttls()
          smtp.login('your_email@gmail.com', 'your_password')
          smtp.send_message(email)
          print('message sent')
    ```

<h1 id='hashlib'>hashlib - Hash Password</h1>

[Go Back to Summary](#summary)

-   Python has a built-in library called `hashlib` that helps us to hash our password
-   [hashlib - Official Docs](https://docs.python.org/3/library/hashlib.html)

<h2 id='passwordchecker'>Password Checker</h2>

[Go Back to Summary](#summary)

-   Checks if our password has been leaked
-   [Hash Generator](https://passwordsgenerator.net/md5-hash-generator/)
-   `hashlib.sha1(password.encode('utf-8')).hexdigest().upper()`

    -   basically we get our `password` and then encode as `utf-8` (we must provide an encode), then we convert into hexadecimal digits, and then covert everything to uppercase

-   now we can get the first 5 character and the rest of the password (tail)
    -   `first5_char, tail = sha1password[:5], sha1password[5:]`
-   Then we send a quest to the api to return the of leaked passwords,
-   After that we check if there is any hash equal to our hashed password

    ```Python
      import requests
      import hashlib
      import sys

      def request_api_data(query_data):
          url = 'https://api.pwnedpasswords.com/range/' + query_data
          res = requests.get(url)

          if res.status_code != 200:
              raise RuntimeError(f'Error fetching {res.status_code}. check the api again')

          return res

      def get_password_leaks_count(hashes, my_hashed_pass):
          hashes = (line.split(':') for line in hashes.text.splitlines())

          for hash, count in hashes:
              if hash == my_hashed_pass:
                  return count
          return 0

      def pwned_api_check(password):
          sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
          first5_char, tail = sha1password[:5], sha1password[5:]
          response = request_api_data(first5_char)
          return get_password_leaks_count(response, tail)

      def main(passwords):
          for password in passwords:
              count = pwned_api_check(password)
              if count:
                  print(f'{password} was fount {count} times... you should change your password')
              else:
                  print(f'{password} was NOT found')
          return 'done!'

      main(sys.argv[1:])
    ```
