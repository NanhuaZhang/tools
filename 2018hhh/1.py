inputs = []
while True:
    num = raw_input()
    if num == '':
        break
    inputs.append(int(num))
num0 = 0
for num in inputs:
    if num == 0:
        num0 += 1
    else:
        print(num)
while num0 > 0:
    print(0)
    num0 -= 1

