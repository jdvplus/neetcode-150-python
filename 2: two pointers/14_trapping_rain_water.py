'''
https://leetcode.com/problems/trapping-rain-water/description/
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
'''

from typing import List
from collections import deque

# time complexity - O(n)
# space complexity - O(1)

def trap(heights: List[int]) -> int:
  l, r = 0, len(heights) - 1
  max_left, max_right = heights[l], heights[r]
  water = 0

  while l < r:
    if max_left <= max_right:
      l += 1
      max_left = max(max_left, heights[l])
      water += max_left - heights[l]
    else:
      r -= 1
      max_right = max(max_right, heights[r])
      water += max_right - heights[r]
  
  return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # should log: 6
print(trap([4,2,0,3,2,5])) # should log: 9

# ultra brute force solution - O(n^2) time complexity, O(n) space complexity
# (non-two pointers solution)
def trap2(heights: List[int]) -> int:
  water = 0
  max_left, max_right = [0], deque([0])

  for i in range(1, len(heights)):
    max_left.append(max(heights[:i]))
  for i in range(len(heights) - 1, 0, -1):
    max_right.appendleft(max(heights[i:]))
  
  for i in range(len(heights)):
    min_val = min(max_left[i], max_right[i])
    diff = min_val - heights[i]
    
    if diff > 0:
      water += diff
  
  return water

print(trap2([0,1,0,2,1,0,1,3,2,1,2,1])) # should log: 6
print(trap2([4,2,0,3,2,5])) # should log: 9