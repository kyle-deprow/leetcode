from typing import List

class Solution:
  def canJump(self, nums: List[int]) -> bool:
    # Replace nums array with an array showing maximum jump given that
    # You can either go with current ind value + the value at that spot of the array
    # or by using the previous value of jump
    for i in range(1, len(nums)):
      nums[i] = max(nums[i] + i, nums[i-1])
    
    ind = 0
    ans = 0
    # Now that the array is constructed, iterate through array until you are farther than
    # the end, signifying that you could reach n-1 index if you wanted
    while ind < len(nums)-1:
      ans += 1
      ind = nums[ind]
    return ans

if __name__ == '__main__':
  s = Solution()
  test_nums = [2,3,1,1,4]
  val = s.canJump(test_nums)
  print(val)