from typing import List
from collections import defaultdict

# Solution involves traversing list and attaching values to hash map to track
# connecting vertices.  Once we traverse the list, we analyze the map to
# find points with only a single adjacent value.  We know that these are
# the edge cases of the list.  Once we find these values, we can traverse
# the map one final time, using adjacent values, to construct the original array
class Solution:
  def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
    adj_map = defaultdict(set)
    # build map
    for i, j in adjacentPairs:
      adj_map[i].add(j)
      adj_map[j].add(i)
    # find edges
    for k, v in adj_map.items():
      if len(v) == 1:
        cur_key = k
        break
    # build array
    arr = [None]*len(adj_map)
    i = 0
    arr[i] = cur_key
    while adj_map[cur_key]:
      i += 1
      val = adj_map[cur_key].pop()
      arr[i] = val
      adj_map[val].remove(cur_key)
      cur_key = val
    return arr

if __name__ == '__main__':
  s = Solution()
  test = [[2,1],[3,4],[3,2]]
  val = s.restoreArray(test)
  print(val)