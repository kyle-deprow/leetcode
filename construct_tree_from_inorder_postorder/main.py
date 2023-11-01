from typing import List, Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  
  def __str__(self):
    return '[TreeNode val={v}, left={l}, right={r}]'.format(v=self.val, l=self.left, r=self.right)

class Solution:
  def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    if inorder:
      # Use root of preorder to split inorder tree view to build left and right recursively
      ind = inorder.index(postorder.pop(-1))
      root = TreeNode(val=inorder[ind])
      root.right = self.buildTree(inorder=inorder[ind+1:], postorder=postorder)
      root.left = self.buildTree(inorder=inorder[:ind], postorder=postorder)
      return root

if __name__ == '__main__':
  s = Solution()
  test_inorder = [9,3,15,20,7]
  test_postorder = [9,15,7,20,3]
  val = s.buildTree(test_inorder, test_postorder)
  print(val)