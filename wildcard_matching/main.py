from typing import List

class Solution:
  def __init__(self):
    self.memo = {}

  def f(self, s: str, p: str) -> bool:
    # Memoization solution involves storing previous iterations
    # return value if exists already
    if (s, p) in self.memo:
      return self.memo[(s, p)]
    # Base case where the pattern immediately matches the string
    if (s == p):
      self.memo[(s, p)] = True
    # If p is a singular wildcard, then all matches with it
    elif (p == '*'):
      self.memo[(s, p)] = True
    # Bottom level case where we've iterated all of the way through
    # either the string or the pattern
    elif ((s == "" and p != "") or (s != "" and p == "")):
      self.memo[(s, p)] = False
    # Case where first letter matches pattern first letter (or ?)
    # iteratively check next character string
    elif (s[0] == p[0] or p[0] == '?'):
      self.memo[(s, p)] = self.f(s[1:], p[1:])
    # Case where first letter of pattern has wildcard, iterate through
    # two branches where one goes through the rest of the string,
    # and the other through the rest of the pattern
    elif (p[0] == '*'):
      self.memo[(s, p)] = self.f(s[1:], p) or self.f(s, p[1:])
    # No matches, case is false
    else:
      self.memo[(s, p)] = False
    return self.memo[(s, p)]

  def isMatch(self, s: str, p: str) -> bool:
    # Filter loop to replace ignore repeating wildcards
    filtered_pattern = ''
    for i in range(0, len(p)):
      if i == 0:
        filtered_pattern = p[i]
      else:
        if p[i] == '*' and p[i-1] == '*':
          continue
        else:
          filtered_pattern += p[i]
    return self.f(s, filtered_pattern)

if __name__ == '__main__':
  s = Solution()
  test_s = 'aa'
  test_p = 'a'
  test_val = s.isMatch(test_s, test_p)
  print(test_val)