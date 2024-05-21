'''
https://leetcode.com/problems/contains-duplicate/description/

217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''

from typing import List

def containsDuplicate(nums: List[int]) -> bool:
  if len(nums) < 2 or len(nums) == len(set(nums)):
    return False
  
  return True

print(containsDuplicate([1,2,3,1])) # should log: True
print(containsDuplicate([1,2,3,4])) # should log: False

def containsDuplicate2(nums: List[int]) -> bool:
  if len(nums) < 2:
    return False
  
  unique = set()

  for n in nums:
    if n in unique:
      return True
    
    unique.add(n)
  
  return False

print(containsDuplicate2([1,2,3,1])) # should log: True
print(containsDuplicate2([1,2,3,4])) # should log: False