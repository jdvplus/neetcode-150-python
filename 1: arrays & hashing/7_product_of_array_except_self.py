'''
https://leetcode.com/problems/product-of-array-except-self/description/
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

from typing import List

# time complexity - O(n)
# space complexity - O(1), not counting output array

def product_except_self(nums: List[int]) -> List[int]:
  ans = [1] * len(nums)

  prefix, postfix = 1, 1

  # handle prefix: iterate over nums
  # reassign curr ans value to prefix, then reassign prefix
  for i in range(len(nums)):
    ans[i] = prefix
    prefix *= nums[i]
  
  # handle postfix: iterate over nums backwards
  # reassign curr ans value to itself * postfix, then reassign postfix
  for i in range(len(nums) - 1, -1, -1):
    ans[i] *= postfix
    postfix *= nums[i]

  return ans

print(product_except_self([1,2,3,4])) # should log: [24, 12, 8, 6]
print(product_except_self([-1,1,0,-3,3])) # should log: [0, 0, 9, 0, 0]
