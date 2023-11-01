from typing import List

class Solution:
  def canJump(self, nums: List[int]) -> bool:
    reachable = 0
    for i in range(len(nums)):
      if i > reachable: return False
      reachable = max(reachable, i + nums[i])
      if reachable > len(nums)-1:
        break
    return True

if __name__ == '__main__':
  s = Solution()
  test_nums = [2,3,1,1,4]
  val = s.canJump(test_nums)
  print(val)