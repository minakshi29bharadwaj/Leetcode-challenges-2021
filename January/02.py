#
# Given two binary trees original and cloned and given a reference to a node target in the original tree.
#
# The cloned tree is a copy of the original tree.
#
# Return a reference to the same node in the cloned tree.
#
# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.
#
# Follow up: Solve the problem if repeated values on the tree are allowed.
# 
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 10^4].
# The values of the nodes of the tree are unique.
# target node is a node from the original tree and is not null.
#
#
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not cloned or cloned.val == target.val and original is target:
            return cloned
        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)
