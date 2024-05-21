'''
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

def isAnagram(s: str, t: str) -> bool:
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

print(isAnagram('anagram', 'nagaram')) # should log: True
print(isAnagram('rat', 'car')) # should log: False

def isAnagram2(s: str, t: str) -> bool:
  return Counter(s) == Counter(t)

print(isAnagram2('anagram', 'nagaram')) # should log: True
print(isAnagram2('rat', 'car')) # should log: False