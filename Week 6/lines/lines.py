import sys

def main():
    file = get()
    lines = read(file)
    print(lines)

def get():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")  
    if not (sys.argv[1]).endswith(".py"):
        sys.exit("Not a Python file")
    return sys.argv[1]

def read(file):
    try:
        with open(file) as file:
            l = 0
            for line in file:
                if line.strip().startswith("#"):
                    continue
                elif line.rstrip() == (""):
                    continue
                else:
                    l += 1
        return l
    except FileNotFoundError:
        sys.exit("File does not exit")

main()