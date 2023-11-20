from typing import List

# Straightforward problem where we iterate through the word dict
# and pluck out words as we see them in the string.  Perform memo
# to efficiently store if strings are in the word for faster execution.
class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    self.memo = {}
    wordDict.sort(reverse=True)
    return self.dp(s, wordDict)
  
  def dp(self, s, wordDict):
    print(s, wordDict, self.memo)
    if s in self.memo:
      return self.memo[s]
    if not s:
      return True
    for word in wordDict:
      if s.startswith(word):
        new_s = s[len(word):]
        if self.wordBreak(new_s, wordDict):
          self.memo[word] = True
          return True
    self.memo[word] = False
    return False

if __name__ == '__main__':
  s = Solution()
  #test_s = 'applepenapple'
  #test_dict = ['apple', 'pen']
  #test_s = 'catsandog'
  #test_dict = ['cats', 'and', 'dog', 'sand', 'cat']
  test_s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
  test_dict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
  test_val = s.wordBreak(test_s, test_dict)
  print(test_val)