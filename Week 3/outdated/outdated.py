def main():
    list = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
    ]
    while True:
        try:
            x = input("Date: ").lower().strip()
            if " " in x:
                month,day,year = x.split(" ")
                month = list.index(month) + 1
                day = int(day.replace(",",""))
                year = int(year)
            else:
                month,day,year = map(int,x.split("/"))
            if 0 < month < 13 and 0 < day < 32 and 0 < year:
                print(f"{year}-{month:02}-{day:02}")
                break
            pass
        except ValueError:
            pass
main()
