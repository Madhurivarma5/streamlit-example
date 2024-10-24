class Tnode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def create(arr, i, n):
    if i < n:
        temp = Tnode(arr[i])  
        node = temp
        node.left = create(arr, 2*i + 1, n)
        node.right = create(arr, 2*i + 2, n)

        return node
    return None
arr = [11, 12, 5, 7, 10, 11, 12, 14]
root = create(arr, 0, len(arr))
 
def post_order(node):
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.val, end=' ')

def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node.val, end=' ')
    in_order(node.right)

def pre_order(node):
    if not node:
        return
    print(node.val, end=' ')
    pre_order(node.left)
    pre_order(node.right)

print()
post_order(root)
print()
in_order(root)
print()
pre_order(root)
