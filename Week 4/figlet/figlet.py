import sys
from random import randint
from pyfiglet import Figlet
def main():
    x = Figlet()
    l = x.getFonts()
    
    if len(sys.argv) == 1:
        y = l[randint(0,len(l))]
        
    elif len(sys.argv) == 3:
        if sys.argv[1] not in ("-f","--font") or sys.argv[2] not in l:
                sys.exit("Invalid Usage")
        y = sys.argv[2]

    else:
        sys.exit("Invalid Usage")
        
    x.setFont(font=y)
    print(x.renderText(input()))          
main()           

    

