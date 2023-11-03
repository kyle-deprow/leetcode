# Solution involves a sliding window where the right most index is
# incremented every iteration.  The substring collected from the left
# and right indexes is then analyzed for repeating chars by comparing
# the length of the substring against the string filtered for repeating
# chars.  If the substring has been determined to have repeating chars
# increment the left index as well to drop the left most character, else
# record length of substring if larger than previous and increment right
# index only.
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    i = 0
    j = 0
    ans = 0
    while j < len(s):
      # Pythonic way to compare length of substring against a filtered version
      # (obtained by set and then reconverted to string using "".join())
      if len(s[i:j+1]) == len("".join(set(s[i:j+1]))):
        ans = max(ans, j-i+1)
      else:
        i += 1
      j += 1
    return ans

if __name__ == '__main__':
  s = Solution()
  test_s = ' '
  val = s.lengthOfLongestSubstring(test_s)
  print(val)