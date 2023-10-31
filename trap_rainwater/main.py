from typing import List

class Solution:
  def trap(self, heights: List[int]) -> int:
    # Create potential trapping map
    potential = {i: 0 for i in range(max(heights)+1)}
    trapped = 0
    # Initialize left side wall
    wall = heights[0]
    prev_h = wall

    for h in heights[1:]:
      # Two conditions to check for
      # If the current height is less than the highest left side wall
      # increment potential trappings
      # If the current height increased, add any potentials to the
      # trapped total.
      if h < wall:
        for i in range(wall - h):
          potential[wall - i] += 1
      if h > prev_h:
        for i in range(h + 1):
          trapped += potential[i]
          # zero out potentials after adding to total
          potential[i] = 0
        # set wall to new max if increased
        wall = max(wall, h)
      prev_h = h
    return trapped

# Two pointer solution where we check whether the left side wall is the max or the right
# if the left side is the max then we know that the water added happens when the height
# drops below the rmax, vice-versa when right side is max
class Solution2:
  def trap(self, heights: List[int]) -> int:
    lmax = 0
    rmax = 0
    l = 0
    r = len(heights) - 1
    trapped = 0
    # Loop until left pointer passes right
    while l < r:
      lmax = max(lmax, heights[l])
      rmax = max(rmax, heights[r])
      if lmax < rmax:
        trapped += lmax - heights[l]
        # move left pointer to right
        l += 1
      else:
        trapped += rmax - heights[r]
        # move right pointer to left
        r -= 1
    return trapped

if __name__ == '__main__':
  s = Solution2()
  test_h = [0,1,0,2,1,0,1,3,2,1,2,1]
  trapped = s.trap(test_h)
  print(trapped)