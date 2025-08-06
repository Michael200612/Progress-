def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not 1 < len(s) < 7:
        return False
    if not s[0:2].isalpha():
        return False
    if "0" in s and s[s.index("0")-1].isnumeric() == False:
        return False
    for i in s:
        if not i.isnumeric() and not i.isalpha():
            return False
        if i.isnumeric() and s[s.index(i):len(s)].isnumeric() == False:
            return False
    return True
   
if __name__ == "__main__":
    main()