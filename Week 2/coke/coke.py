def main():
    x = 50
    while x > 0:
        print(f"Amount Due: {x}")
        z = int(input("Insert Coin: "))
        match z:
            case 5|10|25:
                x -= z
    print(f"Change Owed: {abs(x)}")
main()


