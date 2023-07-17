# https://leetcode.com/problems/two-sum/  1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# import numpy as np

class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]: #slow (37%) - great on memory
    # Runtime 942 ms Beats 37.84% # Memory 17.1 MB Beats 93.95%
    for index, number in enumerate(nums):
      second_number = target - number
      #second_number index cannot equal current index
      if second_number in nums and nums.index(second_number) != index:
        return [index, nums.index(second_number)]
        
solution=Solution()
r1 = solution.twoSum([11,7,15,2], 9) # [1,3]
r2 = solution.twoSum([3,2,4], 6) # [1,2]
r3 = solution.twoSum([3,3], 6) # [0,1]

print(r1)
print(r2)
print(r3)