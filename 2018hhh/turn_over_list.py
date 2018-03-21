# while True:
#     num = int(raw_input())
#     nums = [int(x) for x in raw_input().split(' ')]
#     sort_nums = sorted(nums)
#     indexes = []
#     for index in range(num):
#         if nums[index] != sort_nums[index]:
#             indexes.append(index)
#     reverse_list = list(reversed(nums[indexes[0]:indexes[-1]+1]))
#     if reverse_list == sort_nums[indexes[0]:indexes[-1]+1]:
#         print("yes")
#     else:
#         print("no")
while True:
    num = int(raw_input())
    # nums = [int(x) for x in raw_input().split(' ')]
    nums = map(int, raw_input().split())
    print(nums)
    sort_nums = sorted(nums)
    if nums == sort_nums:
        print("yes")
        break
    for index in range(num):
        if nums[index] != sort_nums[index]:
            start = index
            break
    for index in reversed(range(num)):
        if nums[index] != sort_nums[index]:
            end = index
            break
    reverse_list = list(reversed(nums[start:end+1]))
    nums[start:end+1] = reverse_list
    if nums == sort_nums:
        print("yes")
    else:
        print("no")

n = int(raw_input())
ns = map(int,raw_input().split())
sorted_ns = sorted(ns)
for index in range(n):
    if ns[index] != sorted_ns[index]:
        start = index
        break

for index in reversed(range(n)):
    if ns[index] != sorted_ns[index]:
        end = index
        break
ns[start:end+1] = reversed(ns[start:end+1])
if ns==sorted_ns:
    print 'yes'
else:
    print 'no'