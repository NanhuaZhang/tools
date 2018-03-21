while True:
    input_num = int(raw_input())
    index = 1
    temp = input_num
    while temp > 0:
        temp -= index
        index += 1
    last_day = sum(range(index)) - (index-2)*2
    if temp == -1:
        print(last_day+1)
    elif temp == -2 or temp == 0:
        print(last_day)
    else:
        print(last_day+temp+2)
