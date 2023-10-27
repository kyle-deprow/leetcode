from typing import List
import numpy as np

class Solution1:
  def maxProfit(self, prices: List[int]) -> int:
    exp_return = [n for n in (np.subtract(prices[1:], prices[:-1])) if n > 0]
    return max(sum(exp_return), 0)

class Solution2:
  def maxProfit(self, prices: List[int]) -> int:
    rval = 0
    for i in range(len(prices[1:])):
      if prices[i+1] > prices[i]:
        rval += prices[i+1] - prices[i]
    return rval


if __name__ == '__main__':
  s = Solution2()
  test_prices = [7,1,5,3,6,4]
  test_output = 7
  output = s.maxProfit(test_prices)
  print(test_output, output)

  test_prices = [1,2,3,4,5]
  test_output = 4
  output = s.maxProfit(test_prices)
  print(test_output, output)

  test_prices = [7,6,4,3,1]
  test_output = 0
  output = s.maxProfit(test_prices)
  print(test_output, output)

