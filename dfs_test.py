
# class Solution(object):
#     def binaryTreePaths(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[str]
#         """
#         def construct_paths(root, path):
#             if root:
#                 path += str(root.val)
#                 if not root.left and not root.right:
#                     paths.append(path)
#                 else:
#                     path += '->'
#                     construct_paths(root.left, path)
#                     construct_paths(root.right, path)
#
#         paths = []
#         construct_paths(root, '')
#         return paths


def outer():
    num = 12
    def inner(num):
        num = num+10
    inner(num)
    print(num)

outer()


class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_val = 9999
        t_level = 0


        def dfs(node):
            nonlocal t_level,min_val
            t_level= t_level+1
            if node:
                if t_level ==1:
                    min_val = node.val
                else:
                    if abs(node.val-min_val) < min_val:
                        min_val = abs(node.val-min_val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return min_val