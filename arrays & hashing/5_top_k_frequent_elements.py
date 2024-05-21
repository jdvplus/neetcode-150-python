'''
https://leetcode.com/problems/top-k-frequent-elements/description/
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique. 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

from typing import List
from collections import defaultdict

# time complexity - O(n)
# space complexity - O(n)

def top_k_frequent(nums: List[int], k: int) -> List[int]:
  freqs = defaultdict(int)
  # create list to hold frequency buckets (strategy: bucket sort)
  freq_buckets = [[] for i in range(len(nums) + 1)]

  # populate freqs dict with num-freq pairs (can use Counter too)
  for n in nums:
    freqs[n] += 1
 
  # populate frequency buckets with corresponding numbers
  for n, c in freqs.items():
    freq_buckets[c].append(n)
  
  res = []

  # iterate backwards through freq_buckets list to get most frequent nums
  # (can disregard 0th list, because num freq will never be 0)
  for i in range(len(freq_buckets) - 1, 0, -1):
    # if number exists in bucket, push into result
    # once res length becomes equal to k, return result
    for n in freq_buckets[i]:
      res.append(n)

      if len(res) == k:
        return res
      
print(top_k_frequent([1,1,1,2,2,3], 2)) # should log: [1, 2]
print(top_k_frequent([1], 1)) # should log: [1]