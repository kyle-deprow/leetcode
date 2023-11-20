from typing import List

# Solution to this problem is a dfs where by knowing the length of the request
# we can generate the permutations of the parenthesis in this example.
# Perform iterative searches knowing the possible configurations and append when
# the len of the resultant string is n*2 (to account for 2xn charactures '(', ')')
class Solution:
  def __init__(self):
    self.res = []
    self.n = 0

  def generateParenthesis(self, n: int) -> List[str]:
    self.n = n
    self.dfs(0, 0, '')
    return self.res

  def dfs(self, left: int, right: int, s) -> None:
    if len(s) == self.n*2:
      return self.res.append(s)
    
    if left < self.n:
      self.dfs(left + 1, right, s + '(')
    
    if right < left:
      self.dfs(left, right + 1, s + ')')

if __name__ == '__main__':
  s = Solution()
  test = 3
  test_val = s.generateParanthesis(test)
  print(test_val)