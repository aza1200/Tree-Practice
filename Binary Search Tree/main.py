class Node:
    def __init__(self,data):
        self.data  = data
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self.insert_value(self.root,data)
        return self.root is not None

    def insert_value(self,node,data):
        if node is None:
            node = Node(data)
        else:
            if data<= node.data:
                node.left = self.insert_value(node.left,data)
            else:
                node.right = self.insert_value(node.right,data)
        return node

    def find(self,key):
        return self.find_value(self.root,key)

    def find_value(self,root,key):
        if root is None:
            return False
        elif root.data == key:
            return True
        elif key < root.data:
            return self.find_value(root.left,key)
        else:
            return self.find_value(root.right,key)

    def delete(self,key):
        self.root,deleted = self.delete_value(self.root,key)
        return deleted

    def delete_value(self,node,key):

        if node is None:
            return node,False

        deleted = False

        if key == node.data:
            deleted = True

            if node.left and node.right:

                parent,child = node,node.right

                while child.left is not None:
                    parent,child = child,child.left

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
            node.left,deleted = self.delete_value(node.left,key)
        else:
            node.right,deleted = self.delete_value(node.right,key)
        return node,deleted

    def print(self): # 왼쪽 가운데 오른쪽 순회
        def in_order_traversal(root):
            if root is None:
                pass
            else:
                in_order_traversal(root.left)
                print(root.data,end=" ")
                in_order_traversal(root.right)
        in_order_traversal(self.root)

if __name__ == "__main__":

    arr = [5, 2, 4, 22, 10, 12, 15, 60, 44, 9]
    bst = BinarySearchTree()
    for i in arr:
        bst.insert(i)

    #
    # print(bst.find(61)) # False
    # print(bst.find(22)) # True
    # print(bst.find(60)) # True
    # print(bst.delete(60)) # True
    # print(bst.find(60)) # False
    # print(bst.delete(22)) # True
    # print(bst.delete(44)) # True
    # print(bst.find(22)) # False
    # print(bst.find(44)) # False

    bst.print()

