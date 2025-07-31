def main():
    list = []
    #I couldn't find the modern prices
    dict = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
    while True:
        try:
            x = input("Item: ").lower().strip()
            if x in dict:
                list.append(dict[x])
                print(f"Total: ${sum(list)}")
        except EOFError:
            print("\n")
            break

main()
