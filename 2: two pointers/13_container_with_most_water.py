'''
https://leetcode.com/problems/container-with-most-water/
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
'''

from typing import List

# time complexity - O(n)
# space complexity - O(1)

def max_area(heights: List[int]) -> int:
  maximum_area = 0
  
  l, r = 0, len(heights) - 1

  while l < r:
    height = min(heights[l], heights[r]) # height is min val between heights
    width = r - l # width is r - l (actual indexes)
    area = height * width

    maximum_area = max(maximum_area, area)

    if heights[l] < heights[r]:
      l += 1
    else:
      r -= 1

  return maximum_area

print(max_area([1,8,6,2,5,4,8,3,7])) # should log: 49
print(max_area([1,1])) # should log: 1

# brute force solution - O(n^2) time complexity , O(1) space complexity
def max_area2(heights: List[int]) -> int:
  maximum_area = 0

  for l in range(len(heights)):
    for r in range(l + 1, len(heights)):
      height = min(heights[l], heights[r])
      width = r - l
      area = height * width

      maximum_area = max(maximum_area, area)

  return maximum_area

print(max_area2([1,8,6,2,5,4,8,3,7])) # should log: 49
print(max_area2([1,1])) # should log: 1