x = input("Greeting: ")
if x.strip()[0:5].lower() == "hello":
    print("$0")
elif x.strip()[0:1].lower() == "h":
    print("$20")
else:
    print("$100")
