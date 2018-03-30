def print_matrix(matrix):
    for row in matrix:
        print ' '.join(str(i) for i in row[::-1])


inputs = []
while True:
    num = raw_input()
    if num == '':
        break
    inputs.append(list(num.split()))


print_matrix(zip(*inputs))
