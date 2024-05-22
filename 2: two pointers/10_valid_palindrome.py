'''
https://leetcode.com/problems/valid-palindrome/description/
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
'''

import re

# time complexity - O(n)
# space complexity - O(n)

def is_palindrome(s: str) -> bool:
  # use RegEx to remove non-alphanumeric characters from string
  # and transform to lowercase
  s = re.sub(r'[^a-zA-Z0-9]', '', s).casefold()

  l, r = 0, len(s) - 1

  while l < r:
    if s[l] != s[r]:
      return False
      
    l, r = l + 1, r - 1
  
  return True

print(is_palindrome('A man, a plan, a canal: Panama')) # should log: True
print(is_palindrome('raceacar')) # should log: False
print(is_palindrome(' ')) # should log: True

# helper function: determine if character is alphanumeric
def alpha_num(c: str) -> bool:
  return (ord('A') <= ord(c) <= ord('Z') or
          ord('a') <= ord(c) <= ord('z') or
          ord('0') <= ord(c) <= ord('9'))

def is_palindrome2(s: str) -> bool:
  l, r = 0, len(s) - 1

  while l < r:
    while l < r and not alpha_num(s[l]):
      l += 1
    while r > l and not alpha_num(s[r]):
      r -= 1
    
    if s[l].lower() != s[r].lower():
      return False
    
    l, r = l + 1, r - 1

  return True

print(is_palindrome2('A man, a plan, a canal: Panama')) # should log: True
print(is_palindrome2('raceacar')) # should log: False
print(is_palindrome2(' ')) # should log: True