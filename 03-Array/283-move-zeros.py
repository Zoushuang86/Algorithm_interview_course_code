"""
283. 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""

class Solution:
    # O(n) O(n)
    """
    执行用时：28 ms, 在所有 Python3 提交中击败了94.22%的用户
    内存消耗：15.2 MB, 在所有 Python3 提交中击败了88.68%的用户

    def moveZeroes(self, nums):
        # Do not return anything, modify nums in-place instead.
        nonZerosElements = []
        for i in range(len(nums)):
            if nums[i] != 0:
                nonZerosElements.append(nums[i])
        for j in range(len(nonZerosElements)):
            nums[j] = nonZerosElements[j]

        for k in range(len(nonZerosElements), len(nums)):
            nums[k] = 0
        return nums
    """
    # O(n) O(1)
    """
    执行用时：24 ms, 在所有 Python3 提交中击败了98.64%的用户
    内存消耗：15.3 MB, 在所有 Python3 提交中击败了48.32%的用户
    
    def moveZeroes(self, nums):
        # Do not return anything, modify nums in-place instead.
        k = 0   # nums中，[0,k)为非0元素
        # 遍历到第i个元素后，[0,i]中所有非0元素
        # 都安装顺序排在[0,k)中
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        # 将nums剩余的位置放置0
        for i in range(k, len(nums)):
            nums[i] = 0
        return nums
        """
    """
    def moveZeroes(self, nums):
        # Do not return anything, modify nums in-place instead.
        k = 0  # nums中，[0,k)为非0元素
        # 遍历到第i个元素后，[0,i]中所有非0元素
        # 都安装顺序排在[0,k)中
        # 同时，[k,i]中都为0元素
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
        return nums
    """

    def moveZeroes(self, nums):
        # Do not return anything, modify nums in-place instead.
        k = 0  # nums中，[0,k)为非0元素
        # 遍历到第i个元素后，[0,i]中所有非0元素
        # 都安装顺序排在[0,k)中
        # 同时，[k,i]中都为0元素
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != k:
                    nums[k], nums[i] = nums[i], nums[k]
                k += 1
        return nums


if __name__ == "__main__":
    A = [0, 1, 0, 3, 12]
    s = Solution()
    print(s.moveZeroes(A))
