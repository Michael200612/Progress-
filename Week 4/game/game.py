from random import randint

def main():
    x,y = function1()
    if x:
        function2(y)

def function1():
    while True:
        try:
            x = int(input("Level: "))
            n = randint(1,x)
            return True , n
            break
        except ValueError:
            pass
  
def function2(x):
    while True:
        try:
            y = int(input("Guess: "))
            if y > 0:
                if x > y:
                    print("Too small!")
                elif x < y:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
            pass
        except ValueError:
            pass
     
main()