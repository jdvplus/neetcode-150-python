'''
https://leetcode.com/problems/daily-temperatures/description/
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
'''

from typing import List

# time complexity - O(n)
# space complexity - O(n)

def daily_temperatures(temperatures: List[int]) -> List[int]:
  answer = [0] * len(temperatures)
  stack = [] # stack will store lists of pairs: [temp, idx]

  for i, t in enumerate(temperatures):
    # only pop from stack when curr temp is less than temp at top of stack
    while stack and t > stack[-1][0]: 
      _, stack_i = stack.pop() # destructure
      answer[stack_i] = i - stack_i
    
    stack.append([t, i])
  
  return answer

print(daily_temperatures([73,74,75,71,69,72,76,73])) # should log: [1, 1, 4, 2, 1, 1, 0, 0]
print(daily_temperatures([30,40,50,60])) # should log: [1, 1, 1, 0]
print(daily_temperatures([30,60,90])) # should log: [1, 1, 0]