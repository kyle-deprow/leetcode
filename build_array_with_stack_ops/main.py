from typing import List

# Solution to this involves hash-mapping the desired target allocations
# iterate through an integer array 1->n, if integer in hash map, the we know
# to "Push" it to stack and leave it. In this case, add one to count variable
# to signify another int has been found and move on.  Else if the integer is
# not in the hash map, we know we need to first "Push" that value to the stack
# and then immediately "Pop" it off.  When the count variable is equal to the
# length of the target, we know we've found all the integers necessary.
class Solution:
  def buildArray(self, target: List[int], n: int) -> List[str]:
    ans = []
    target_map = {t: 1 for t in target}
    count = 0
    for i in range(1, n+1):
      # Error handling to determine if integer is a key in map
      try:
        # Integer found, add Pop op and increment count
        if target_map[i]:
          ans += ["Push"]
          count += 1
      except KeyError as e:
        # Integer not found, add Pop and Push ops
        ans += ["Push", "Pop"]
      if count == len(target):
        break
    return ans

if __name__ == '__main__':
  s = Solution()
  test_target = [1,3]
  test_n = 4
  val = s.buildArray(test_target, test_n)
  print(val)