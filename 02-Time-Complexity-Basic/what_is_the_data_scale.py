import time


for x in range(10):
    n = pow(10, x)
    start = time.time()
    sum = 0
    for i in range(n):
        sum += i
    end = time.time()

    print("10^{}:{:.6f}s".format(x, end-start))

"""
输出结果：
10^0:0.000000s
10^1:0.000000s
10^2:0.000000s
10^3:0.000997s
10^4:0.000000s
10^5:0.009552s
10^6:0.086914s
10^7:0.932302s
10^8:9.864830s
10^9:97.252764s
"""