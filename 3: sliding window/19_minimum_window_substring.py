'''
https://leetcode.com/problems/minimum-window-substring/description/
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:
m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

# time complexity - O(n)
# space complexity - O(n)

def min_window(s: str, t: str) -> str:
  if len(t) > len(s): return '' # edge case

  t_count, window_count = {}, {}

  # populate t_count dict (manual Counter)
  for c in t:
    t_count[c] = 1 + t_count.get(c, 0)

  have, need = 0, len(t_count) # need = number of unique chars in 't'
  res, res_len = [0, -1], float('inf')

  l = 0
  for r in range(len(s)):
    # populate window_count dict (manual Counter)
    window_count[s[r]] = 1 + window_count.get(s[r], 0)

    if s[r] in t_count and window_count[s[r]] == t_count[s[r]]:
      have += 1
      
      while have == need:
        # update res_len & res
        if (r - l + 1) < res_len:
          res_len = r - l + 1
          res = [l, r]
        
        # then pop chars from left of window_count
        window_count[s[l]] -= 1
        if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
          have -= 1
        l += 1
  
  l, r = res # destructure updated indexes from res
  return s[l:r+1]

print(min_window('ADOBECODEBANC', 'ABC')) # should log: 'BANC'
print(min_window('a', 'a')) # should log: 'a'
print(min_window('a', 'aa')) # should log: ''
