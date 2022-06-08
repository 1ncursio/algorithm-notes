from typing import Optional


class Node:
    def __init__(
        self, value: int, left: Optional["Node"] = None, right: Optional["Node"] = None
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


class BST:
    """
    Binary Search Tree
    """

    def __init__(self) -> None:
        self.root: "Node" = None

    def search(self, value: int) -> int:
        node = self.root
        while True:
            if not node:
                return -1
            if value == node.value:
                return node.value
            if value < node.value:
                node = node.left
            else:
                node = node.right

    def insert(self, value: int) -> None:
        node = Node(value)
        if not self.root:
            self.root = node
            return

        prev = None
        temp = self.root
        while temp:
            if value < temp.value:
                prev = temp
                temp = temp.left
            elif value > temp.value:
                prev = temp
                temp = temp.right

        if value < prev.value:
            prev.left = node
        else:
            prev.right = node

    def delete(self, value: int) -> Node:
        root = self.root

        # Base Case
        if not root:
            return root

        # Recursive calls for ancestors of
        # node to be deleted
        if value < root.value:
            root.left = self.delete(value, self.root.left)

        elif key > root.key:
            root.right = deleteNode(root.right, key)
            return root

        # We reach here when root is the node
        # to be deleted.

        # If root node is a leaf node

        if root.left is None and root.right is None:
            return None

        # If one of the children is empty

        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # If both children exist

        succParent = root

        # Find Successor

        succ = root.right

        while succ.left != None:
            succParent = succ
            succ = succ.left

        # Delete successor.Since successor
        # is always left child of its parent
        # we can safely make successor's right
        # right child as left of its parent.
        # If there is no succ, then assign
        # succ->right to succParent->right
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right

        # Copy Successor Data to root

        root.key = succ.key

        return root

    def inorder(self):
        temp = self.root
        stack = []
        while temp or stack:
            if temp:
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                print(temp.value, end=" ")
                temp = temp.right


if __name__ == "__main__":
    bst = BST()
    """
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80
       """

    values = [50, 30, 20, 40, 70, 60, 80]
    for value in values:
        bst.insert(value)
    # search
    # print(f"Searching for {values[0]}, result: {bst.search(values[0])}")
    print("Inorder traversal of the given tree")
    bst.inorder()
