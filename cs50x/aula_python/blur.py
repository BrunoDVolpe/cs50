from PIL import Image, ImageFilter

before = Image.open("yard.bmp")
after = before.filter(ImageFilter.BoxBlur(5))
after.save("out.bmp")