from typing import List

def all_equal(lst: List[int]) -> bool:
  return len(set(lst)) <= 1

class Solution1:
  max_duplicates = 2
  def removeDuplicates(self, nums: List[int]) -> int:
    window = self.max_duplicates + 1
    length = len(nums)
    rval = length
    for i in range(length, window-1, -1):
      if all_equal(nums[i-window:i]):
        rval -= 1
        nums[i-1:rval] = nums[i:rval+1]
    return rval

class Solution2:
  def removeDuplicates(self, nums: List[int]) -> int:
    i = 0
    for n in nums:
      if i < 2 or n > nums[i-2]:
        nums[i] = n
        i += 1
    return i

if __name__ == '__main__':
  s1 = Solution1()
  s2 = Solution2()
  test = [1,1,1,2,2,3]
  valid_length_1 = s1.removeDuplicates(test)
  test = [1,1,1,2,2,3]
  valid_length_2 = s2.removeDuplicates(test)
  print(valid_length_1, valid_length_2)
