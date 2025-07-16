x = input("File name: ").strip().lower()
y = x.index(".")
list =  [".gif", ".jpg", ".jpeg", ".png", ".txt"]
list2 = ["pdf", "zip"]
if x[y:] in list:
    print(f"image/{x[y+1:]}")
elif x[y:] in list2:
    print(f"application/{x[y+1:]}")
else:
    print("application/octet-stream")
