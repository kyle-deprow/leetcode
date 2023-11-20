from typing import List, Optional

# The trick to this solution is to ignore the advice about rearranging
# and decrementing the arr. Just use these constraints to understand that
# the max value of the array is minimum of the following three independent
# max value conditions

# Condition 1: the length of the array ultimately determines the max value
# given all other conditions.  The array must at least be of length max value
# since the array must increment every index.

# Condition 2: max value of array

# Condition 3: if the array operations only allow for decrementing, then
# we can use this to determine that, given array size, the max value is
# the second highest value + 1.  Logic being that the highest value is decremented
# to be larger than this
class Solution:
  def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
    change_ind = 0
    arr = sorted(arr)
    for i in range(1, len(arr)):
      if arr[i] > arr[i-1]:
        change_ind = i-1
        max_ind = i
    return min(arr[change_ind]+1, len(arr), arr[max_ind])


if __name__ == '__main__':
  s = Solution()
  test = [209]*9997 + [1] + [9994] + [10000]
  print(s.maximumElementAfterDecrementingAndRearranging(test))