from typing import List

# This problem hinges on the robber having two choices:
# Rob the current house or don't rob the current house
# The former means the robber can't rob the (i-1) house
# but can proceed to the (i-2) house
# If the latter is chosen, the robber can safely rob (i-1)
# Recursive problem where you determine the highest value
# based on the current index in the nums
# Memo (top-down) implementation
class Solution1:
  memo = []
  def rob(self, nums: List[int]) -> int:
    self.memo = [-1]*len(nums)
    return self.rob_recursively(nums, len(nums)-1)

  def rob_recursively(self, nums: List[int], i: int) -> int:
    if (i < 0):
      return 0
    if self.memo[i] >= 0:
      return self.memo[i]
    rval = max(self.rob_recursively(nums, i-2) + nums[i], self.rob_recursively(nums, i-1))
    self.memo[i] = rval
    return rval

# Two variable implementation
class Solution2:
  def rob(self, nums: List[int]) -> int:
    if (len(nums) == 0):
      return 0
    prev1 = 0
    prev2 = 0
    for num in nums:
      temp = prev1
      prev1 = max(prev2 + num, prev1)
      prev2 = temp
    return prev1

if __name__ == '__main__':
  s = Solution1()
  test_list = [1,2,3,1]
  test_val = s.rob(test_list)