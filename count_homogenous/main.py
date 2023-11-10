from typing import List, Optional
from collections import defaultdict

# Two pointer solution that involves moving one pointer along the string
# until a non-homogenous string is created.  In this case, increment a
# global counter with combinations of characters in substring and then reset
# the two pointers.  If hitting the end of the string, move j forward and
# evaluate as if there's a non-homogenous character.
class Solution:
  def update_count(self, i: int, j: int) -> None:
    for k in range(0, j-i):
      self.count += (j-i) - k

  def countHomogenous(self, s: str) -> int:
    self.count = 0
    i = 0
    j = 0
    while j < len(s):
      if s[i] != s[j]:
        self.update_count(i, j)
        i = j
      j += 1
      if j == len(s):
        self.update_count(i, j)
    return self.count % (10e9 + 7)

if __name__ == '__main__':
  s = Solution()
  test_str = 'abbcccaa'
  test_str = 'w'*100000
  val = s.countHomogenous(test_str)
  print(val)