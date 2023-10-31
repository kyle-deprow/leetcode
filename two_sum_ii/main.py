from typing import List

def find_next_unique_index(current_index: int, arr: List[int]) -> int:
  for ind in range(len(arr[current_index+1:])):
    if arr[ind+current_index+1] > arr[current_index]:
      return ind + current_index + 1
  return 10e10

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    i = 0
    while (i < len(numbers)):
      n1 = numbers[i]

      inner_factors = numbers[i+1:]
      j = 0
      while (j < len(inner_factors)):
        n2 = inner_factors[j]
        if n1 + n2 == target:
          return [i+1, j+i+2]
        j = find_next_unique_index(j, inner_factors)

      i = find_next_unique_index(i, numbers)

    # Return a blank list if there are no valid combinations
    return []

class Solution2:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # True 2 pointer solution, designate low and high side pointers
    low, high = 0, len(numbers)-1
    # If Low pointer value crosses high, then break
    while (low < high):
      # Add two pointers and compare
      summation = numbers[low] + numbers[high]
      if summation == target:
        return [low + 1, high + 1]
      # If too large, move high pointer away from end of arr
      elif summation > target:
        high -= 1
      # If too small, move low pointer away from beginning of arr
      elif summation < target:
        low += 1
    return []


if __name__ == '__main__':
  s = Solution2()
  #test_array = [5, 25, 75]
  #test_array = [3,24,50,79,88,150,345]
  #test_array = [-1,0]
  test_array = [-1]*100
  #test_array = [-3,3,4,90]
  #test_array = [-10,-8,-2,1,2,5,6]
  test_target = 0

  ar = s.twoSum(test_array, test_target)
  print(ar)