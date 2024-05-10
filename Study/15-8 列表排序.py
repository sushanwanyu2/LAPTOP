# @Time    : 2024/1/24 10:19
# @Author  : SU_SHAN_WAN_YU
# @File    : 15-8 列表排序.py
# @Description :
'''
冒泡排序:
'''
nums = [5, 1, 7, 6, 8, 2, 4, 3]

for j in range(0, len(nums) - 1):  # 外层循环控制轮数
    for i in range(0, len(nums) - 1 - j):  # 内层循环控制两两比较
        if nums[i] > nums[i + 1]:
            a = nums[i]
            nums[i] = nums[i + 1]
            nums[i + 1] = a  # 底层的机制

# nums.sort()
print(nums)
