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

    def Delete(self, temp, value):
        if value < self.value:
            temp = self
            self.left.Delete(temp, value)
        elif value > self.value:
            temp = self
            self.right.Delete(temp, value)

        else:
            if self.left is None and self.right is None:
                if temp.left == self:
                    temp.left = None
                else:
                    temp.right = None
                self = None

            elif self.right is None:
                if temp.left == self:
                    temp.left = self.left
                else:
                    temp.right = self.left
                self = None

            elif self.left is None:
                if temp.left == self:
                    temp.left = self.right
                else:
                    temp.right = self.right
                self = None

            else:
                temp = self.right
                while temp.left is not None:
                    temp = temp.left
                self.value = temp.value
                self.right.Delete(temp, temp.value)


Root = Tree(6)
Root.Insert(4)
Root.Insert(2)
Root.Insert(5)
Root.Insert(9)
Root.Insert(8)
Root.Insert(10)

print("Inorder traversal after insertion: ", end='')
Root.Inorder(Root)

Root.Delete(Root, 2)
print('\n 2 is deleted: ', end='')
Root.Inorder(Root)

Root.Delete(Root, 4)
print('\n 4 is deleted: ', end='')
Root.Inorder(Root)

Root.Delete(Root, 6)
print('\n 6 is deleted: ', end='')
Root.Inorder(Root)