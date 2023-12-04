def pass_sam(kelly_daily_solutions, sam_daily_solutions):
    kelly_total_solutions = 0
    sam_total_solutions = 0
    day = 0

    while kelly_total_solutions <= sam_total_solutions:
        kelly_total_solutions += kelly_daily_solutions
        sam_total_solutions += sam_daily_solutions
        day += 1

    return day


print(pass_sam(5, 4))