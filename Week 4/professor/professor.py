import random

def main():
    score = 0
    x,y = get_level()
    if x:
        for i in range(10):
            tried = 0
            a,b = generate_integer(y)
            while True:
                if tried == 3:
                        print(f"{a} + {b} = {a + b}")
                        break
                try:
                    n = int(input(f"{a} + {b} = "))
                    if n == a + b:
                        score += 1
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("EEE")
                    tried += 1
        print(f"Score: {score}")

def get_level():
    while True:
        try:
            x = int(input("Level: ")) 
            if x in (1,2,3):
                return True,x
        except:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(1, 9), random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    else:
        return random.randint(100, 999), random.randint(100, 999)

if __name__ == "__main__":
    main()