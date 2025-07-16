x = input("File name: ").strip().lower()
y = x.index(".")
match x[y:]:
    case ".gif" | ".jpg" | ".jpeg"| ".png":
        print(f"image/{x[y+1:]}")
    case ".pdf" | ".zip":
        print(f"application/{x[y+1:]}")
    case ".txt":
        print("document.txt")
    case _:
        print("application/octet-stream")

