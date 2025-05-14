def twoSum(nums, target):
    num_dict = {}
    for index, num in enumerate(nums):
        complement = target - num #计算吧目标值与当前元素差值

        #检查是否在字典中
        if complement in num_dict:
            return [num_dict[complement], index]
        num_dict[num] = index
#e.g
nums1 = [2, 7, 11, 15]
target1 = 9
print(twoSum(nums1, target1))
nums2 = [3, 2, 4]
target2 = 6
print(twoSum(nums2, target2))

nums3 = [3, 3]
target3 = 6
print(twoSum(nums3, target3))