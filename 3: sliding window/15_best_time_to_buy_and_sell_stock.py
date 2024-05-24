'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
'''

from typing import List

# time complexity - O(n)
# space complexity - O(1)

def max_profit(prices: List[int]) -> int:
  profit = 0
  min_price = prices[0]

  for i in range(1, len(prices)):
    if prices[i] > min_price:
      profit = max(profit, prices[i] - min_price)
      
    min_price = min(min_price, prices[i])

  return profit

print(max_profit([7,1,5,3,6,4])) # should log: 5
print(max_profit([7,6,4,3,1])) # should log: 0

# brute force solution - O(n^2) time complexity, O(1) space complexity
def max_profit2(prices: List[int]) -> int:
  profit = 0

  for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
      if prices[j] - prices[i]:
        profit = max(profit, prices[j] - prices[i])
  
  return profit

print(max_profit2([7,1,5,3,6,4])) # should log: 5
print(max_profit2([7,6,4,3,1])) # should log: 0