# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None

        root = TreeNode(preorder[0])
        position_root = inorder.index(preorder[0]) #position de la racine dans le inorder tree
        # on build le subtree:
        root.left = self.buildTree(preorder[1:position_root + 1], inorder[:position_root])
        root.right = self.buildTree(preorder[position_root + 1:], inorder[position_root + 1:])

        return root
        