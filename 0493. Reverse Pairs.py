class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        root = None
        res = 0
        
        class Node:
            def __init__(self, val):
                self.val = val
                self.left = None
                self.right = None
                self.height = 1
                self.cnt = 0
            
        def get_height(root):
            if not root:
                return 0
            return root.height
        
        def get_balance(root):
            return get_height(root.left) - get_height(root.right)
        
        def rotate_left(z):
            y = z.right
            T = y.left
            
            y.left = z
            z.right = T
            
            y.height = 1 + max(get_height(y.left), get_height(y.right))
            z.height = 1 + max(get_height(z.left), get_height(z.right))
            
            return y
        
        def rotate_right(z):
            y = z.left
            T = y.right
            
            y.right = z
            z.left = T
            
            y.height = 1 + max(get_height(y.left), get_height(y.right))
            z.height = 1 + max(get_height(z.left), get_height(z.right))
            
            return y
        
        def insert(root, val):
            if not root:
                return Node(val)
            
            if val < root.val:
                root.left = insert(root.left, val)
            elif root.val < val:
                root.right = insert(root.right, val)
            
            root.height = 1 + max(get_height(root.left), get_height(root.right))
            
            # left left
            if get_balance(root) > 1 and get_balance(root.left) > 0:
                root = rotate_right(root)
            # left right
            elif get_balance(root) > 1 and get_balance(root.left) < 0:
                root.left = rotate_left(root.left)
                root = rotate_right(root)
            # right right
            elif get_balance(root) < -1 and get_balance(root.right) < 0:
                root = rotate_left(root)
            # right left
            elif get_balance(root) < -1 and get_balance(root.right) > 0:
                root.right = rotate_right(root.right)
                root = rotate_left(root)
            
            return root
        
        def search(root, val):
            if not root:
                return 0
            
            if root.val == val:
                return root.cnt
            elif root.val < val:
                return search(root.right, val)
            else:
                return root.cnt + search(root.left, val)
        
        def update(root, val):
            if not root:
                return root
            elif root.val == val:
                root.cnt += 1
            elif root.val < val:
                root.cnt += 1
                root.right = update(root.right, val)
            elif root.val > val:
                root.left = update(root.left, val)
            
            return root
        
        for num in nums:
            root = insert(root, num)
        
        for num in nums:
            res += search(root, 2*num+1)
            root = update(root, num)
        
        return res
