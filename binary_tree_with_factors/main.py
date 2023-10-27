class Solution:
  def numFactoredBinaryTrees(self, arr):
    arr.sort()
    # Initialize factor dictionary with 1
    dct = {elem: 1 for elem in arr}
    # Start with smallest element and iterate through sorted list
    for outer_elem in arr:
      # add in smaller element factors to current outer element
      # if outer_elem is factorable by the inner elem
      for inner_elem in arr:
        # if inner elem == outer elem then move to next outer elem
        if inner_elem == outer_elem:
          break
        # if outer elem is factorable by inner elem and the factor is in
        # the dict, then we know we can build a tree with the inner factor
        # as the root.  Add in possible combinations of this tree to outer
        # element
        if outer_elem % inner_elem == 0 and outer_elem // inner_elem in dct:
          dct[outer_elem] += dct[inner_elem] * dct[outer_elem // inner_elem]
    return sum(dct.values()) % (pow(10, 9) + 7)

if __name__ == '__main__':
  s = Solution()

  test_arr = [2,1,3,5,10,18,40,4,100,1000,565]

  x = s.numFactoredBinaryTrees(test_arr)
  print(x)
