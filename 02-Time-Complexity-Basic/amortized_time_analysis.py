import time


class myVector:
    def __init__(self):
        self.__data = [None for n in range(10)]
        self.__capacity = 10 # 存储数组中可以容纳的最大元素个数
        self.__size = 0

    def push_back(self, e):
        if self.__size == self.__capacity:
            self.__resize(2*self.__capacity)
        self.__data[self.__size] = e
        self.__size += 1

    def pop_back(self):
        assert self.__size > 0
        e = self.__data[self.__size]
        self.__data[self.__size] = None
        self.__size -= 1
        # 防止时间复杂度的震荡
        # if self.__size == self.__capacity // 2:
        #     self.__resize(self.__capacity // 2)
        if self.__size == self.__capacity // 4:
            self.__resize(self.__capacity // 2)
        return e

    # O(n)
    def __resize(self, new_capacity):
        new_data = [None for n in range(new_capacity)]
        new_data[:self.__capacity] = self.__data[:self.__capacity]
        self.__data = None
        self.__data = new_data
        self.__capacity = new_capacity

    def print(self):
        print(self.__data)

"""
for i in range(10, 27):
    n = pow(2, i)
    start = time.time()
    vec = myVector()
    for j in range(n):
        vec.push_back(i)
    end = time.time()
    print("{} operations:\t{:.6f}s".format(2*n, end - start))


输出结果：
2048 operations:	0.000000s
4096 operations:	0.000974s
8192 operations:	0.001998s
16384 operations:	0.003614s
32768 operations:	0.007098s
65536 operations:	0.015282s
131072 operations:	0.028317s
262144 operations:	0.059724s
524288 operations:	0.129254s
1048576 operations:	0.248564s
2097152 operations:	0.502293s
4194304 operations:	1.034762s
8388608 operations:	2.071112s
16777216 operations:	4.153085s
33554432 operations:	8.206884s
67108864 operations:	16.527838s
134217728 operations:	34.544656s
"""
for i in range(10, 27):
    n = pow(2, i)
    start = time.time()
    vec = myVector()
    for j in range(n):
        vec.push_back(i)
    for j in range(n):
        vec.pop_back()
    end = time.time()
    print("{} operations:\t{:.6f}s".format(2*n, end - start))
"""
输出结果：

"""