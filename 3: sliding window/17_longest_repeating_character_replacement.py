'''
https://leetcode.com/problems/longest-repeating-character-replacement/description/
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Constraints:
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
'''

# time complexity - O(n) [technically O(26n)]
# space complexity - O(n)

def character_replacement(s: str, k: int) -> int:
  count = {} # dict to store character counts
  res = 0

  # initialize both L & R pointers at beginning of string
  l = 0
  for r in range(len(s)):
    count[s[r]] = 1 + count.get(s[r], 0) # populate dict

    # window is valid if (window length - max frequency) <= k
    # (window length formula: r - l + 1)
    while (r - l + 1) - max(count.values()) > k:
      count[s[l]] -= 1 # decrement count of current L char before incrementing
      l += 1
    
    res = max(res, r - l + 1) # reassign res to window length if longer

  return res

print(character_replacement('ABAB', 2)) # should log: 4
print(character_replacement('AABABBA', 1)) # should log: 4

# ultra-optimized solution - O(n) time complexity, O(n) space complexity
def character_replacement2(s: str, k: int) -> int:
  count = {}
  res = 0
  max_freq = 0 # store max frequency in variable for O(1) lookup

  l = 0
  for r in range(len(s)):
    count[s[r]] = 1 + count.get(s[r], 0)
    max_freq = max(max_freq, count[s[r]]) # reassign max frequency

    while (r - l + 1) - max_freq > k:
      count[s[l]] -= 1
      l += 1
    
    res = max(res, r - l + 1)

  return res

print(character_replacement2('ABAB', 2)) # should log: 4
print(character_replacement2('AABABBA', 1)) # should log: 4