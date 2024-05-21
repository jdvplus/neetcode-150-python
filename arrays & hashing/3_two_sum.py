'''
https://leetcode.com/problems/two-sum/description/
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
'''

from typing import List

# time complexity - O(n)
# space complexity - O(n)

def two_sum(nums: List[int], target: int) -> List[int]:
  hash_map = {}

  for i, n in enumerate(nums):
    complement = target - n
    if complement in hash_map:
      return [hash_map[complement], i]
    hash_map[n] = i

print(two_sum([2,7,11,15], 9)) # should log: [0, 1]
print(two_sum([3,2,4], 6)) # should log: [1, 2]
print(two_sum([3,3], 6)) # should log: [0, 1]

# brute force solution - O(n^2) time complexity, O(1) space complexity
def two_sum2(nums: List[int], target: int) -> List[int]:
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]
      
print(two_sum2([2,7,11,15], 9)) # should log: [0, 1]
print(two_sum2([3,2,4], 6)) # should log: [1, 2]
print(two_sum2([3,3], 6)) # should log: [0, 1]