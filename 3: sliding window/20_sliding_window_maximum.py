'''
https://leetcode.com/problems/sliding-window-maximum/
239. Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
'''

from typing import List
from collections import deque

# time complexity - O(n)
# space complexity - O(k)

def max_sliding_window(nums: List[int], k: int) -> List[int]:
  res = []
  queue = deque()
  l = r = 0

  while r < len(nums):
    while queue and nums[queue[-1]] < nums[r]:
      queue.pop()
    
    queue.append(r)

    if l > queue[0]:
      queue.popleft()

    if (r + 1) >= k:
      res.append(nums[queue[0]])
      l += 1
    
    r += 1
  
  return res

print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3)) # should log: [3,3,5,5,6,7]
print(max_sliding_window([1], 1)) # should log: [1]

# ultra brute force / intuitive solution
  # O(k * (n - k)) time complexity, O(n - k) space complexity
  # fails LeetCode tests (time limit exceeded)
def max_sliding_window2(nums: List[int], k: int) -> List[int]:
  res = []

  for i in range(len(nums) - k + 1):
    window = nums[i:i+k]
    res.append(max(window))

  return res

print(max_sliding_window2([1,3,-1,-3,5,3,6,7], 3)) # should log: [3,3,5,5,6,7]
print(max_sliding_window2([1], 1)) # should log: [1]