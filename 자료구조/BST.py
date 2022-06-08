from typing import Optional


class BST:
    root = None

    def __init__(self) -> None:
        self.root: Node = None
        self.__size = 0

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

    def insert(self, value: int) -> bool:
        if not self.root:
            self.root = Node(value, None, None)
            self.__size += 1
            return True

        # 루트가 있다면 들어가삼
        node = self.root
        while True:
            # 중복값 방지
            if value == node.value:
                return False
            if value < node.value:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(value, None, None)
                    self.__size += 1
                    return True
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(value, None, None)
                    self.__size += 1
                    return True

    def remove(self, value: int) -> bool:
        pass

    def dump(self):
        def print_subtree(node: Node) -> None:
            # 전위 순회로 출력
            if node:
                print(
                    f"{node.value} {node.left.value if node.left else None} {node.right.value if node.right else None}"
                )
                print_subtree(node.left)
                print_subtree(node.right)

        root = self.root
        print_subtree(root)

    # length
    def __len__(self):
        return self.__size


class Node:
    def __init__(self, value: int, left, right) -> None:
        self.value = value
        self.left = left
        self.right = right


if __name__ == "__main__":
    bst = BST()
    values = [50, 15, 62, 80, 7, 54, 11]
    for value in values:
        print(f"Tried to insert {value}, result: {bst.insert(value)}")
    # search
    print(f"Searching for {values[0]}, result: {bst.search(values[0])}")
    bst.dump()
