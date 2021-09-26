import time


# def binary_search(arr, n, target):
#     left, right = 0, n-1    # 在[left, right]的范围里寻找target
#     while left <= right:    # 当left==right，区间[left, right]依然是有效的
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         if target > arr[mid]:
#             left = mid + 1  # target在[mid+1,right]中
#         else:
#             right = mid - 1 # target在[left,mid-1]中
#     return -1


# def binary_search(arr, n, target):
#     left, right = 0, n    # 在[left, right)的范围里寻找target
#     while left < right:    # 当left==right，区间[left, right)是无效的
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         if target > arr[mid]:
#             left = mid + 1  # target在[mid+1,right)中
#         else:
#             right = mid     # target在[left,mid)中
#     return -1

def binary_search(arr, n, target):
    left, right = 0, n    # 在[left, right)的范围里寻找target
    while left < right:    # 当left==right，区间[left, right)是无效的
        mid = left + (right - left) // 2    # 防止整型溢出
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            left = mid + 1  # target在[mid+1,right)中
        else:
            right = mid     # target在[left,mid)中
    return -1


arr = [n for n in range(100000000)]
start = time.time()
binary_search(arr, 100000000, 666666)
end = time.time()
print("{:.6f}s".format(end-start))  # 0.001004s
