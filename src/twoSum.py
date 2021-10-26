'''
Created on Oct 26, 2021

@author: rishikasurineni
'''
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    
    def helper(nums,target,i,j):
        for i,j in nums[i],nums[i+1]:
            if nums[i]+nums[j] == target:
                return [i,j]
        else:
            helper(nums, target, i+1,j)
            