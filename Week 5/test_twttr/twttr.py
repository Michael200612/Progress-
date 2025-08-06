def main():
    x = shorten(input("Input: "))
    print(f"Output: {x}")

def shorten(word):
    for char in word:
        if char.lower() in ["a","e","i","o","u"]:
            word = word.replace(char,"")
    return word

if __name__ == "__main__":
    main()