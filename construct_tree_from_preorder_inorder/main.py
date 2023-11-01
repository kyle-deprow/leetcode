from typing import List, Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  
  def __str__(self):
    return '[TreeNode val={v}, left={l}, right={r}]'.format(v=self.val, l=self.left, r=self.right)

class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if inorder:
      # Use root of preorder to split inorder tree view to build left and right recursively
      ind = inorder.index(preorder.pop(0))
      root = TreeNode(val=inorder[ind])
      root.left = self.buildTree(preorder=preorder, inorder=inorder[:ind])
      root.right = self.buildTree(preorder=preorder, inorder=inorder[ind+1:])
      return root

if __name__ == '__main__':
  s = Solution()
  test_preorder = [3,9,20,15,7]
  test_inorder = [9,3,15,20,7]
  val = s.buildTree(test_preorder, test_inorder)
  print(val)