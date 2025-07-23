def main():
    snake(input("camelCase: ").strip())

def snake(string):
    for i in string:
        if i.isupper():
           string = string.replace(i,"_"+i.lower())
    print(f"snake_case: {string}")
main()

