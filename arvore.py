class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def contar_nos_recursivo(root):
    if root is None:
        return 0
    return 1 + contar_nos_recursivo(root.left) + contar_nos_recursivo(root.right)

def maior_valor_iterativo(root):
    if root is None:
        return None
    max_value = float('-inf')
    stack = [root]
    while stack:
        node = stack.pop()
        max_value = max(max_value, node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return max_value

def busca_recursiva(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    return busca_recursiva(root.left, target) or busca_recursiva(root.right, target)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

print("Número de nós na árvore:", contar_nos_recursivo(root))
print("Maior valor na árvore:", maior_valor_iterativo(root))
print("O número 7 está na árvore:", busca_recursiva(root, 7))
print("O número 10 está na árvore:", busca_recursiva(root, 10))