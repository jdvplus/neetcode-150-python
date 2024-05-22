'''
https://leetcode.com/problems/longest-consecutive-sequence/description/
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''

from typing import List

# time complexity - O(n)
# space complexity - O(n)

def longest_consecutive(nums: List[int]) -> int:
  lookup = set(nums) # utilize set for O(1) lookup
  longest = 0

  for n in nums:
    if n - 1 not in lookup: # if prev num isn't present, it means we've begun a sequence
      length = 0

      while (n + length) in lookup:
        length += 1

      longest = max(length, longest)

  return longest

print(longest_consecutive([100,4,200,1,3,2])) # should log: 4
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1])) # should log: 9
