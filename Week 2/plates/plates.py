def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 1 < len(s) < 7:
        if s[0:2].isalpha():
            if "0" in s and s[s.index("0")-1].isnumeric() == False:
                return False
            else:
                for i in s:
                    if i.isnumeric() == False and i.isalpha() == False:
                        return False
                    if i.isnumeric() and s[s.index(i):len(s)].isnumeric() == False:
                        return False
                return True
   
main()
