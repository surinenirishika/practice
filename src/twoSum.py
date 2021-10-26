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
    if nums[0]+nums[1] == target:
        return [0,1]
    else:
        self.twoSum(nums+1, target)
            
