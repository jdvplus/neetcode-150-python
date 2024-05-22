'''
https://leetcode.com/problems/3sum/description/
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
'''

from typing import List

# time complexity - O(n^2)
# space complexity - O(1), excluding space required for input & output

def three_sum(nums: List[int]) -> List[List[int]]:
  nums.sort()
  res = []

  for i, n in enumerate(nums):
    # edge cases:
      # 1. if curr num is greater than 0, no other possible triplets
      # 2. ensure no duplicate triplets
    if n > 0:
      return res
    if i > 0 and n == nums[i - 1]:
      continue

    l, r = i + 1, len(nums) - 1

    while l < r:
      total = n + nums[l] + nums[r]

      if total == 0:
        res.append([n, nums[l], nums[r]])
        l += 1

        # ensure no duplicate triplets
        while nums[l] == nums[l - 1] and l < r:
          l += 1
      
      if total < 0:
        l += 1
      if total > 0:
        r -= 1

  return res

print(three_sum([-1,0,1,2,-1,-4])) # should log: [[-1,-1,2],[-1,0,1]]
print(three_sum([0,1,1])) # should log: []
print(three_sum([0,0,0])) # should log: [[0, 0, 0]]
print(three_sum([0, 0, 0, 0])) # should log: [[0, 0, 0]]