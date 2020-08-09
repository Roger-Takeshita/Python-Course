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