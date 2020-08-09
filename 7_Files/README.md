<h1 id='summary'>Summary</h1>

-   [Image Processing](#imageprocessing)
    -   [Installation](#installpil)
    -   [PIL Basics](#pilbasics)
    -   [Image Converter (jpg to png](#imageconverter)

<h1 id='imageprocessing'>Image Processing</h1>

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
      filtered_img.save('./converted/yumi_blur.png', 'png')

      #! Smooth
      filtered_img2 = img.filter(ImageFilter.SMOOTH)
      filtered_img2.save('./converted/yumi_smooth.png', 'png')

      #! Sharpen
      filtered_img3 = img.filter(ImageFilter.SHARPEN)
      filtered_img3.save('./converted/yumi_sharpen.png', 'png')

      #! Grey Scale
      filtered_img4 = img.convert('L') # 'L' = grey scale
      filtered_img4.save('./converted/yumi_grey_scale.png', 'png')

      #! Show Image
      # filtered_img4.show()

      #! Rotate
      rotated_img = filtered_img4.rotate(75)
      rotated_img.save('./converted/yumi_rotated.png', 'png')

      #! Resize
      resized_img = img.resize((300, 300))
      resized_img.save('./converted/yumi_300x300.png', 'png')

      #! Crop
      box = (100, 100, 400, 400)
      cropped_img = img.crop(box)
      cropped_img.save('./converted/yumi_cropped.png', 'png')

      #! Thumbnail
      img.thumbnail((150 ,150))
      img.save('./converted/yumi_thumbnail.png')
    ```

<h2 id='imageconverter'>Image Converter (jpg to png)</h2>

[Go Back to Summary](#summary)

-   To use the image converter, we first need to import the `sys` module to get the input from the user
-   We need to import `os` or `pathlib` (alternative)
    -   [os - Official Docs](https://docs.python.org/3/library/os.html)
    -   [pathlib - Official Docs](https://docs.python.org/3/library/pathlib.html)
-   To use run the code we need to give the images_folder and the destination folder, like so:
-   `python3 image_converter.py images_jpg/ images_png/`

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
