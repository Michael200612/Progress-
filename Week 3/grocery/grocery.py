def main():
    list = []
    while True:
        try:
            list.append(input().strip().upper())
        except EOFError:
            for i in set(list):
                 print(f"{list.count(i)} {i.upper()}")
            break
main()



