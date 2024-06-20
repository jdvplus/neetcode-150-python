'''
https://leetcode.com/problems/valid-parentheses/description/
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
'''

# time complexity - O(n)
# space complexity - O(k), where k is max number of successive opening brackets in 's'

def is_valid(s: str) -> bool:
  brackets = {
    '(': ')',
    '{': '}',
    '[': ']'
  }
  stack = []

  for c in s:
    if c in brackets:
      stack.append(c)
    else:
      if not len(stack) or brackets[stack.pop()] != c:
        return False
  
  return not len(stack)

print(is_valid('()')) # should log: True
print(is_valid('()[]{}')) # should log: True
print(is_valid('(]')) # should log: False