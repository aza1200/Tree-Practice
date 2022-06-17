from model.binary_tree import BinarySearchTree

if __name__ == "__main__":

    arr = [5, 2, 4, 22, 10, 12, 15, 60, 44, 9]
    bst = BinarySearchTree()
    for i in arr:
        bst.insert(i)


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

