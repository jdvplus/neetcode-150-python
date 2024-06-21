'''
https://leetcode.com/problems/generate-parentheses/description/
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
'''

from typing import List

# time complexity - O(4^n / math.sqrt(n))
# space complexity - O(n)

def generate_parentheses(n: int) -> List[str]:
  res = []

  def backtrack(s: str, open_n: int, closed_n: int) -> None:
    if open_n == closed_n == n:
      res.append(s)
      return
    
    if open_n < n:
      backtrack(s + '(', open_n + 1, closed_n)
    
    if closed_n < open_n:
      backtrack(s + ')', open_n, closed_n + 1)
  
  backtrack('', 0, 0)
  return res

print(generate_parentheses(3))
  # should log: ['((()))','(()())','(())()','()(())','()()()']
print(generate_parentheses(1)) # should log: ['()']