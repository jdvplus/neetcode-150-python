'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
'''

from collections import defaultdict

# time complexity - O(n)
# space complexity - O(n)

def length_of_longest_substring(s: str) -> int:
  seen = set()
  l = 0
  res = 0

  # initialize both L & R pointers at beginning of string
  for r in range(len(s)):
    while s[r] in seen:
      seen.remove(s[l]) # s[l] must be the same as s[r], so remove it
      l += 1
    
    seen.add(s[r])
    res = max(res, r - l + 1)
  
  return res

print(length_of_longest_substring('abcabcbb')) # should log: 3
print(length_of_longest_substring('bbbbb')) # should log: 1
print(length_of_longest_substring('pwwkew')) # should log: 3

# brute force / intuitive solution - O(n) time complexity, O(n) space complexity
def length_of_longest_substring2(s: str) -> int:
  if not s:
    return 0
  
  if s.isspace():
    return 1
  
  substrings = defaultdict(int)
  i, prev_start = 0, 0
  curr_seen = set()

  while i < len(s):
    if s[i] not in curr_seen:
      curr_seen.add(s[i])
      i += 1
    else:
      substrings[s[prev_start:i]] = len(curr_seen)
      curr_seen.clear()
      prev_start += 1
      i = prev_start
  
  if curr_seen:
    substrings[s[prev_start:i]] = len(curr_seen)
  
  return max(substrings.values())

print(length_of_longest_substring2('abcabcbb')) # should log: 3
print(length_of_longest_substring2('bbbbb')) # should log: 1
print(length_of_longest_substring2('pwwkew')) # should log: 3
