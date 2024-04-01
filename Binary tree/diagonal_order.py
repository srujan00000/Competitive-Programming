from collections import deque
class TreeNode:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
def diagonal_order(root):
    if not root:
        return []
    result=[]
    queue=deque([(root,0)])
    while queue:
        node,level=queue.popleft()
        if level==len(result):
            result.append([])
        result[level].append(node.val)
        if node.left:
            queue.append((node.left,level+1))
        if node.right:
            queue.append((node.right,level))
    return result