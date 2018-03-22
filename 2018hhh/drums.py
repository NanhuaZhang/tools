while True:
    nums = [int(x) for x in raw_input().split()]
    n = nums[0]
    m = nums[1]

    opt = [[0]*31 for _ in range(31)]
    opt[0][0] = 1
    for i in range(1, m+1):
        for j in range(n):
            if j == 0:
                opt[i][j] = opt[i-1][1] + opt[i-1][n-1]
            elif j == n-1:
                opt[i][j] = opt[i-1][n-2] + opt[i-1][0]
            else:
                opt[i][j] = opt[i-1][j-1] + opt[i-1][j+1]
    print(opt[m][0])
