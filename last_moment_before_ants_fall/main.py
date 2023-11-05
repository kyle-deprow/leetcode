from typing import List

# Solution involves ignoring the advice that ants turn
# around in collision and understanding that holistically
# ants still execute their paths even if it's not the original
# ant.  In this case, we just need to find the max path from
# the edge for all ants on the left and right and return the max
class Solution1:
  def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
    # find max of left (default being 0 if empty) and the max path of right
    # being the length of the board - min(right) with default being n if empty
    # return max of these two values
    return max(max(left, default=0), n-min(right, default=n))

if __name__ == '__main__':
  s = Solution1()
  test_right =  [0,1]
  test_left = [4,3]
  test_n = 4
  test_val = s.getLastMoment(test_n, test_left, test_right)