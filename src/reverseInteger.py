'''
Created on Oct 26, 2021

@author: rishikasurineni
'''
#
def reverse(x:int) -> int:
    
    num = 0
    sign = 1
    if x < 0:
        sign = -1
        x = -1*x
    while x > 0:
        mod_dig = x % 10
        num = num * 10 + mod_dig
        x = x // 10
    return sign*num
    if not -2147483648<x<2147483648:
        return 0
        