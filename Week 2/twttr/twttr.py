def main():
    x = input("Input: ")
    for char in x:
        if char.lower() in ["a","e","i","o","u"]:
            x = x.replace(char,"")
    print(f"Output: {x}")
main()
