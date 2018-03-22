# coding=utf-8

while True:
    a = list(raw_input())
    b = list(raw_input())
    flag = 1
    for ch in set(b):
        if b.count(ch) > a.count(ch):
            flag = 0
            print(flag)
            break
    if flag:
        print(flag)
