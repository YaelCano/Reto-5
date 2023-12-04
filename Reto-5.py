def min_num(sam_daily, kelly_daily, difference):
    if kelly_daily <= sam_daily:
        return -1

    days = 0
    sam_solved = difference
    kelly_solved = 0

    while sam_solved >= 0:
        sam_solved += sam_daily
        kelly_solved += kelly_daily
        difference = sam_solved - kelly_solved
        days += 1

        if difference <= 0:
            return days

    return -1

sam_daily = int(input("Enter Sam's daily solved problems:"))
kelly_daily = int(input("Enter Kelly's daily solved problems:"))
difference = int(input("Enter the initial difference in solved problems (Sam ahead):"))

result = min_num(sam_daily, kelly_daily, difference)

print(f"Minimum number of days for Kelly to surpass Sam: {result}")