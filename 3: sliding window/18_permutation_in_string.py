'''
https://leetcode.com/problems/permutation-in-string/description/
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
'''

from collections import Counter

# time complexity - O(n)
# space complexity - O(1)

def check_inclusion(s1: str, s2: str) -> bool:
  if len(s1) > len(s2): return False

  s1_count, s2_count = [0] * 26, [0] * 26
  for i in range(len(s1)):
    s1_count[ord(s1[i]) - ord('a')] += 1
    s2_count[ord(s2[i]) - ord('a')] += 1

  matches = 0
  for i in range(26):
    matches += (1 if s1_count[i] == s2_count[i] else 0)
  
  l = 0
  for r in range(len(s1), len(s2)):
    if matches == 26: return True

    index = ord(s2[r]) - ord('a')
    s2_count[index] += 1
    if s1_count[index] == s2_count[index]:
      matches += 1
    elif s1_count[index] + 1 == s2_count[index]:
      matches -= 1

    index = ord(s2[l]) - ord('a')
    s2_count[index] -= 1
    if s1_count[index] == s2_count[index]:
      matches += 1
    elif s1_count[index] - 1 == s2_count[index]:
      matches -= 1
    
    l += 1
  
  return matches == 26

print(check_inclusion('ab', 'eidbaooo')) # should log: True
print(check_inclusion('ab', 'eidboaoo')) # should log: False

# intuitive solution - O(n * m) time complexity, O(n) space complexity
  # where n = len(s1) and m = len(s2)
def check_inclusion2(s1: str, s2: str) -> bool:
  l, r = 0, len(s1) - 1

  while r < len(s2):
    window_str = s2[l:r+1]

    if Counter(s1) == Counter(window_str):
      return True

    l += 1
    r += 1
  
  return False

print(check_inclusion2('ab', 'eidbaooo')) # should log: True
print(check_inclusion2('ab', 'eidboaoo')) # should log: False
