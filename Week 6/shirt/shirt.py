import sys
from PIL import Image, ImageOps
from os.path import splitext

def main():
    x,y = get()
    function(x,y)

def get():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not splitext(sys.argv[1].lower())[1] in (".png",".jpeg",".jpg") or not splitext(sys.argv[2].lower())[1] in (".png",".jpeg",".jpg"):
        sys.exit("Invalid input")
    if splitext(sys.argv[1])[1] != splitext(sys.argv[2])[1]:
        sys.exit("Input and output have different extensions")
    return sys.argv[1], sys.argv[2]

def function(x,y):
    try:
        img = Image.open(x)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt = Image.open("shirt.png")
    size = shirt.size
    m = ImageOps.fit(img, size)
    m.paste(shirt, shirt)
    m.save(y)

main()