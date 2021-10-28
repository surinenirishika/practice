'''
Created on Oct 27, 2021

@author: rishikasurineni
'''
def sortColors(self, nums: list[int]): 
    
    self.nums = nums
    r = []
    w = []
    b = []
    
    for i in range(nums.length - 1):
        if nums[i] == 0:
            r.append(nums[i])
        elif nums[i] == 1:
            w.append(nums[i])
        elif nums[i] == 2:
            b.append(nums[i])
        else:
            return None
        return r+w+b
    


print(sortColors([2,0,2,1,1,0]))
    