'''
https://leetcode.com/problems/valid-anagram/description/
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
'''

from collections import defaultdict, Counter

# time complexity - O(n), where n is total number of characters
# space complexity - O(n), where n is total number of unique characters (max 26)

def is_anagram(s: str, t: str) -> bool:
  if len(s) != len(t):
    return False
  
  countS, countT = defaultdict(int), defaultdict(int)

  for i in range(len(s)):
    countS[s[i]] += 1
    countT[t[i]] += 1

  for char in countS:
    if countS[char] != countT[char]:
      return False
    
  return True

print(is_anagram('anagram', 'nagaram')) # should log: True
print(is_anagram('rat', 'car')) # should log: False

# solution using Counter dict subclass (counts hashable objects)
def is_anagram2(s: str, t: str) -> bool:
  return Counter(s) == Counter(t)

print(is_anagram2('anagram', 'nagaram')) # should log: True
print(is_anagram2('rat', 'car')) # should log: False