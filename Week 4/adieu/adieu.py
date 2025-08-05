import inflect

def main():
    list = []
    while True:
        try:
            x = input("Name: ")
            list.append(x)
        except EOFError:
           break

    p = inflect.engine()
    print(f"Adieu, adieu, to {p.join(list)}")

main()