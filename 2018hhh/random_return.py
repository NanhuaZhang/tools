import random
return_data = {
    501: 0,
    502: 1,
    503: 1,
    504: 1,
    505: 1,
    510: 1
}


def mock_interface_return(dic: dict):
    values = dic.values()
    interval = 100//sum(values)
    random_num = random.randint(0, 99-(100 % sum(values))) % 100
    value = random_num//interval
    for key in dic:
        if value <= 0:
            return key
            # break
        value -= int(dic[key])


while True:
    key = mock_interface_return(return_data)
    print(key)
    # if key == '501':
    #     break
