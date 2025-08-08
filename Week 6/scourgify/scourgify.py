import sys
import csv

def main():
    x,y = get()
    write(read(x),y)
    
def get():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Invalid file type")
    return sys.argv[1:]

def read(x):
    try:
        l = []
        with open(x) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last,first = row["name"].split(",")
                l.append([first, last, row["house"]])
        return l
    except FileNotFoundError:
        sys.exit(f"Cannot read {x}")

def write(l,y):
    try:
        with open(y, "w", newline = '') as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for i in l:
                    writer.writerow({"first": i[0], "last": i[1], "house": i[2]})
    except:
        sys.exit("Error")

main()