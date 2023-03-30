class Tree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def Inorder(self, Root):
        if Root is None:
            return
        self.Inorder(Root.left)
        print(Root.value, end=' ')
        self.Inorder(Root.right)

    def Insert(self, value):
        if self is None:
            self = Tree(value)
        elif value < self.value:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.Insert(value)
        else:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.Insert(value)


Root = Tree(6)
Root.Insert(4)
Root.Insert(2)
Root.Insert(5)
Root.Insert(9)
Root.Insert(8)
Root.Insert(10)

print("Inorder traversal after insertion: ", end='')
Root.Inorder(Root)