import os
import sys
from pathlib import Path

sys.path.append(str(Path(os.path.abspath(__file__)).parent.parent))

from model.tree import Node


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert_value(self.root, data)
        return self.root is not None

    def insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self.insert_value(node.left, data)
            elif data > node.data:
                node.right = self.insert_value(node.right, data)
        return node

    def find(self, key):
        return self.find_value(self.root, key)

    def find_value(self, root, key):
        if root is None:
            return False
        elif root.data == key:
            return True
        elif key < root.data:
            return self.find_value(root.left, key)
        elif key > root.data:
            return self.find_value(root.right, key)

    def delete(self, key):
        self.root, deleted = self.delete_value(self.root, key)
        return deleted

    #  오른쪽 서브트리의 가장 왼쪽 노드 를 삭제하려는 위치에 집어넣는다
    # 1. 왼쪽 서브트리 를 오른쪽서브트리의 가장왼쪽 노드에 붙이기
    # 삭제할 노드와 오른쪽 서브트리의 왼쪽노드의 부모가 다를시
    # 2. 오른쪽 서브트리의 가장왼쪽노드의 부모의 왼쪽노드자리에 가장왼쪽노드의 오른쪽 자식 붙이기
    # 3. 해당 자식의 오른쪽 자리에 삭제할노드의 오른쪽 붙이기
    def delete_value(self, node, key):

        if node is None:
            return node, False

        deleted = False

        if key == node.data:
            deleted = True

            if node.left and node.right:

                parent, child = node, node.right

                while child.left is not None:
                    parent, child = child, child.left

                child.left = node.left

                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self.delete_value(node.left, key)
        else:
            node.right, deleted = self.delete_value(node.right, key)
        return node, deleted

    def print(self):
        # 왼쪽 가운데 오른쪽 순회
        def in_order_traversal(root):
            if root is None:
                pass
            else:
                in_order_traversal(root.left)
                print(root.data, end=" ")
                in_order_traversal(root.right)
        in_order_traversal(self.root)
