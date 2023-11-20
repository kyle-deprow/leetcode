from typing import List

# Solution to this problem relies on understanding that palindromes
# have a center which can be exploited.  If we expand out from each
# point in the string and compare max palindromes to saved ones, then we
# will find the longest. The only trick to this is accounting for even
# palindromes ("bb" in "abb") so we need to run the logic twice where
# the center is between the index and the next index (i and i+1)
class Solution:
  def expand(self, s: str, left_i: int, right_i: int) -> str:
    while left_i >= 0 and right_i < len(s) and s[left_i] == s[right_i]:
      left_i -= 1
      right_i += 1
    return s[left_i+1:right_i]

  def longestPalindrome(self, s: str) -> str:
    if len(s) == 1:
      return s
    
    max_str = s[0]
    for i in range(len(s) - 1):
      odd = self.expand(s, i, i)
      even = self.expand(s, i, i+1)
      if len(odd) > len(max_str):
        max_str = odd
      if len(even) > len(max_str):
        max_str = even
    return max_str

if __name__ == '__main__':
  s = Solution()
  test = 'babad'
  test_val = s.longestPalindrome(test)
  print(test_val)