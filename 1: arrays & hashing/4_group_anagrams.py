'''
https://leetcode.com/problems/group-anagrams/description/
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

from typing import List
from collections import defaultdict

# time complexity - O(m * n)
# space complexity - O(m * n)
  # m = length of 'strs' list
  # n = average length of each string

def group_anagrams(strs: List[str]) -> List[List[str]]:
  res = defaultdict(list)

  for s in strs:
    # create array of 26 zeroes representing frequency of alphabetic chars in curr string
    count = [0] * 26

    for char in s:
      # update value of curr character in curr string
      # (ord returns unicode num representation of char)
      count[ord(char) - ord('a')] += 1

    # create k-v pairs in res dict such that:
      # key - tuple representing specific char frequencies of a given string
      # value - list containing strings associated with specific tuple
    # i.e.:
      # (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
      # is the tuple associated with: ['eat', 'tea', 'ate']
    res[tuple(count)].append(s)
  
  return res.values()

print(group_anagrams(['eat','tea','tan','ate','nat','bat']))
  # should log: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(group_anagrams([''])) # should log: [['']]
print(group_anagrams(['a'])) # should log: [['a']]