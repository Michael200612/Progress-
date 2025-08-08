import sys
import PIL
from os.path import splitext

def main():
    x,y = get()
    read(x,y)

def get():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not splitext(sys.argv[1])[1] in (".png",".jpeg",".jpg") or not splitext(sys.argv[2])[1] in (".png",".jpeg",".jpg"):
        sys.exit("Invalid input")
    if splitext(sys.argv[1])[1] != splitext(sys.argv[2])[1]:
        sys.exit("Input and output have different extensions")
    return sys.argv[1], sys.argv[2]

def read(x,y):
    Pil.Image.open(x)

def write():
    ...

main()