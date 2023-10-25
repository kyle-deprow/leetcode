from typing import List

class Solution:
  def rotate(self, nums: List[int], k:int) -> None:
    length = len(nums)
    k = k%length
    nums[0:length-k] = reversed(nums[0:length-k])
    nums[length-k:] = reversed(nums[length-k:])
    nums[:] = reversed(nums[:])

if __name__ == '__main__':
  s1 = Solution()
  test = [1,2,3,4,5,6,7]
  print(test)
  s1.rotate(test, 3)
  print(test)

  test = [-1,-100,3,99]
  print(test)
  s1.rotate(test, 2)
  print(test)

  test = [1,2]
  print(test)
  s1.rotate(test, 5)
  print(test)