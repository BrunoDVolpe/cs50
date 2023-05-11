#wget https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png
#wget https://cs50.harvard.edu/python/2022/psets/6/shirt/muppets.zip
#unzip muppets.zip
from os.path import splitext
import sys
from PIL import Image
from PIL import ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif splitext(sys.argv[1])[1].lower() not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid input")
elif splitext(sys.argv[2])[1].lower() not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid input")
elif splitext(sys.argv[1])[1].lower() != splitext(sys.argv[2])[1].lower():
    sys.exit("Input and output have different extensions")
else:
    try:
        with Image.open(sys.argv[1]) as im:
            pass
    except FileNotFoundError:
        sys.exit("File not found")

with Image.open("shirt.png") as shirt:
    with Image.open(sys.argv[1]) as photo:
        size = shirt.size
        new_photo = ImageOps.fit(photo,size)
#        new_photo.save("res_and_croped.jpg") #teste para ver imagem intermediária
        new_photo.paste(shirt, shirt)
        new_photo.save(sys.argv[2])

"""
#Internet mostra muito assim
shirt = Image.open("shirt.png")
photo = Image.open(sys.argv[1])
size = shirt.size
new = ImageOps.fit(photo, size)
new.paste(shirt,shirt)
new.save(sys.argv[2])
"""