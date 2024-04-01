class Treenode:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
def print_leaves(root,result):
    if root:
        print_leaves(root.left,result)
        if not root.left and not root.right:
            result.append(root.val)
        print_leaves(root.right,result)
def print_left_boundary(root,result):
    if root:
        if root.left:
            result.append(root.val)
            print_left_boundary(root.left,result)
        elif root.right:
            result.append(root.val)
            print_left_boundary(root.right,result)
def print_right_boundary(root,result):
    if root:
        if root.right:
            print_right_boundary(root.right,result)
            result.append(root.val)
        elif root.left:
            print_left_boundary(root.left,result)
            result.append(root.val)
def boundary_traversal(root):
    if not root:
        return []
    res=[root.val]
    print_left_boundary(root.left,res)
    print_leaves(root,res)
    print_right_boundary(root.right,res)