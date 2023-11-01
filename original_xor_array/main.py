from typing import List

# Simple in-array manipulation with the trick being
# to revert an XOR operation, you commute the operation
# due to the communicative property of XOR. i.e.
# c = a ^ b where ^ represents XOR
# a = c ^ b
# b = c ^ a

# To save space, you can perform this in-array using 2
# swap variables to store the values of the prev position
class Solution:
  def findArray(self, pref: List[int]) -> List[int]:
    tmp1 = pref[0]
    for i in range(1, len(pref)):
      tmp2 = pref[i]
      pref[i] = pref[i] ^ tmp1
      tmp1 = tmp2
    return pref

if __name__ == '__main__':
  s = Solution()
  test_array = [5,2,0,3,1]
  print(s.findArray(test_array))