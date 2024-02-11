from Node import Node
from BinarySearchTree import BinarySearchTree


def main():

    bst = BinarySearchTree()

    node = Node()
    node.set_value(10)

    bst.insert(node)
    bst.print_bst()

    bst.delete(node)
    bst.print_bst()


if __name__ == '__main__':
    main()
