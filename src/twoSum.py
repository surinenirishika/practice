'''
Created on Oct 26, 2021

@author: rishikasurineni
"""
:type nums: List[int]
:type target: int
:rtype: List[int]
'''
def twoSum(nums: list[int], target: int) -> list[int]:
       
    nums1 = []
    i = 0
    j = 1
    while i <= len(nums)-2 and j <= len(nums)-1:
        if nums[i]+nums[i+1] == target:
            nums1.append(i)
            j = i+1
            nums1.append(j)
            return nums1
        else:
            j += 1
            i += 1
    return nums1
print(twoSum([2,7,11,13],9))
print(twoSum([3,2,4], 6))