from typing import List

# Trick to this solution involves determining the X and Y (horizontal and vertical)
# distances from the target.  Once this is calculated, we know that diagonal movements
# move x and y one unit towards the target.  Once we can no longer traverse diagonally
# then we either move in the x or y direction until reaching the target.  These
# movements are then added together to determine the minimal amount of movements(time)
# required, which we then compare to t
class Solution:
  def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
    if sx == fx and sy == fy:
        return t > 1 or t == 0

    y_diff = abs(sy - fy)
    x_diff = abs(sx - fx)

    mov_still_req = abs(y_diff - x_diff)

    return (min(y_diff, x_diff) + mov_still_req) <= t

if __name__ == '__main__':
  s = Solution()
  sx = 3
  sy = 1
  fx = 7
  fy = 3
  t = 3
  val = s.isReachableAtTime(sx, sy, fx, fy, t)
  print(val)