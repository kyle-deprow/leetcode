from typing import List

# Solution could be reached many ways, but given the execution time
# restraint of O(n) algorithm complexity, we must proitize solutions
# over others.  Brute forcing this problem with repeat indexing (O(n^2))
# or sorting algorithms (O(nlogn)) are immediate non-starters.  Hash
# mapping and unordered sets become obvious targets from here

# Solution below involves creating an unordered set from nums and then
# iterating through nums.  The set does 2 things, first it removes duplicates
# second it creates a hashing lookup so traversal of the set happens in linear
# time.  This allows us to compare individual num in nums to efficiently evaluate
# if they exist in the set, but more importantly to determine if the preceding int
# value (num-1) exists. If it does, then we know we are not at a starting point of
# a consecutive list.  If it doesn't, then this num is the starting point and we
# can loop through all consecutive numbers to determine the length of the chain.
# Return the longest running chain in nums.
class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
      return 0

    ans = 1

    num_set = set(nums)
    for num in nums:
      if num - 1 not in num_set:
        chain_length = 1
        chain_start = num

        while chain_start + chain_length in num_set:
          chain_length += 1
      
      ans = max(ans, chain_length)

    return ans


if __name__ == '__main__':
  s = Solution()
  test_nums = [100,4,200,1,3,2]
  test_val = s.longestConsecutive(test_nums)
  print(test_val)