def triangles():
    l = [1]
    while True:
        yield l
        l.append(0)
        l = [l[i-1]+l[i] for i in range(len(l))]


line_index = 0
for line in triangles():
    if line_index < 10:
        line_index += 1
    else:
        break
    print(line)
