from typing import List

# Solution involves maintaining a map of all available characters
# in a particular word and appending the word to the map given
# these characters as a key.  To standardize the keying, we sort
# the word alphabetically to create a universal key among all anagrammed
# words
class Solution1:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    char_map = {}
    for word in strs:
      # Python sorted function returns list of characters
      # sorted alphabetically, we need to use join to convert
      # back to a string
      sorted_word = ''.join(sorted(word))
      if sorted_word in char_map: char_map[sorted_word] += [word]
      else: char_map[sorted_word] = [word]
    # return all values in map as a list of lists
    return list(char_map.values())

# Learned this one today, collections has a defaultdict object to handle
# the annoying key checking that you must do with dictionaries when
# looking to append.  We don't even need to store the sorted word anymore
from collections import defaultdict
class Solution2:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # Create defaultdict that will default all unseen keys to a list
    char_map = defaultdict(list)
    
    for word in strs:
      char_map[''.join(sorted(word))] += [word]
    
    return list(char_map.values())

if __name__ == '__main__':
  s = Solution2()
  test_list = ['eat','tea','tan','ate','nat','bat']
  test_val = s.groupAnagrams(test_list)
  print(test_val)