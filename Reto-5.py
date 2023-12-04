def sam_y_kelly(sam, kelly, diferencia):

    sam_result = diferencia + sam
    kelly_result = kelly
    dias = 1
    while kelly_result < sam_result:
        dias += 1
        sam_result = sam_result + 3
        kelly_result = kelly_result + 5
        print(sam_result, kelly_result, dias)
    return dias

print("Kelly will pass Sam on day", sam_y_kelly(3, 5, 5))