from collections import deque
class TreeNode:
	def __init__ (self,val):
		self.val=val 
		self.left=None
		self.right=None

	
def spiral_level_order(root):
	if not root:
		return []
	result=[]
	queue=deque([root])
	left_to_right=True
	while queue:
		level_size=len(queue)
		current_level=deque()
		for _ in range(level_size):
			node=queue.popleft()
			if left_to_right:
				current_level.append(node.val)
			else:
				current_level.appendleft(node.val)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		result.append(list(current_level))
		left_to_right=not left_to_right
	return result