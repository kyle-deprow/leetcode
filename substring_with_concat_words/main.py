from typing import List

# Naive solution to this involves finding all permutations of input word array
# Once we have this list of permutations, create a sliding window and compare
# the substring captured in the window to permutation array. Problem with this
# is finding permutations is O(n^2) task and given lots of input words, this
# becomes very inefficient.  Better solution is create a hash map of input words
# and then sub-slice windows of the input string to m many words where m is the
# word count expected in the substring and utilizing the fact that the words all
# have the same length, we know the substring has length m*l where l is
# len(words[0]) == len(words[1]) == .. len(words[n-1])

# once we have a complete and split substring list, iteratively decrement counts
# in the hash map and add index to the answer if the sum of the hashmap is equal
# to zero or we have accounted for all of the words in the substring
class Solution:
  def findSubstring(self, s: str, words: List[str]) -> List[int]:
    word_map = {}
    for word in words:
      if word in word_map: word_map[word] += 1
      else: word_map[word] = 1

    word_count = len(words)
    word_size = len(words[0])
    ans = []
    for i in range(len(s) - word_count*word_size + 1):
      # Python comprehension to slide across a sliding window and create indexed
      # lists capturing character groups of word_size in substring of size 
      # word_count*word_size
      substr_list = [s[i+j*word_size:i+(j+1)*word_size] for j in range(word_count)]
      map_copy = word_map.copy()
      for word in substr_list:
        # if word is in our word_map, then decrement.  When all values are zero
        # in map, then we know that we have observed every word in words in
        # windowed substring
        if word in map_copy and map_copy[word] > 0: map_copy[word] -= 1
        else: break
        if sum(map_copy.values()) == 0:
          ans.append(i)
    return ans

if __name__ == '__main__':
  s = Solution()
  #test_s = 'barfoothefoobarman'
  #test_words = ['bar', 'foo']
  #test_s = 'wordgoodgoodgoodbestword'
  #test_words = ['word', 'good', 'best', 'word']
  #test_s = 'barfoofoobarthefoobarman'
  test_s = "barfoofoobarthefoobarman"
  #test_words = ['bar', 'foo', 'the']
  test_words = ["bar","foo","the"]
  # test_s = 'wordgoodgoodgoodbestword'
  # test_words = ['word', 'good', 'best', 'good']
  val = s.findSubstring(test_s, test_words)
  print(val)