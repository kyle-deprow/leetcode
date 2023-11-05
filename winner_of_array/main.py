from typing import List

# Solution involves two pointer solution where you repeatedly compare
# value of arr[i] vs arr[j] where i and j start as 0 and 1 respectively.
# If arr[i] wins, increment ans_i and move j forward 1. If i loses,
# reset ans_i to 1 (to account for arr[j] winning), move i to j, and
# j forward one. To account for the looping nature of the problem where
# losers are queued at the end of the array, we simply just reset j to
# index 0 when reaching the end of the array and if j == i at any point
# move it forward one. We can also take advantage of short-circuiting
# the entire process if k if large and we've seen ans_i > len(arr) since
# we know subsequent loops will only result in more arr[i] wins
class Solution:
  def getWinner(self, arr: List[int], k) -> int:
    i = j = 0
    ans_i = 0
    while i < len(arr) and ans_i != k and ans_i < len(arr):
      # If j hits the end of the arr, move to beginning
      if j >= len(arr):
        j = 0
      # If j is equal to i, move 1 forward
      if j == i:
        j += 1
      # Perform comparison, if larger move j forward
      # if not, reset ans_i to 1, move i to j and move j forward one
      if arr[i] > arr[j]:
        ans_i += 1
        j += 1
      else:
        ans_i = 1
        i = j
        j = i + 1
    return arr[i]

if __name__ == '__main__':
  s = Solution()
  #test_arr = [2,1,3,5,4,6,7]
  #test_k = 2
  #test_arr = [3,2,1]
  #test_k = 10
  test_arr = [1,11,22,33,44,55,66,77,88,99]
  test_k = 10000000
  test_val = s.getWinner(test_arr, test_k)
  print(test_val)