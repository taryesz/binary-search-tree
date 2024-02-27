from Node import Node
from BinarySearchTree import BinarySearchTree


def main():

    bst = BinarySearchTree()

    node0 = Node()
    node1 = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    node5 = Node()

    node0.set_value(10)
    bst.insert(node0)

    node1.set_value(5)
    bst.insert(node1)

    node5.set_value(4)
    bst.insert(node5)

    node2.set_value(15)
    bst.insert(node2)

    node3.set_value(13)
    bst.insert(node3)

    node4.set_value(14)
    bst.insert(node4)

    # 0 - bfs      --> 10 5 15 4 13 14
    # 1 - dfs+in   --> 4 5 10 13 14 15
    # 2 - dfs+pre  --> 10 5 4 15 13 14
    # 3 - dfs+post --> 4 5 14 13 15 10

    bst.print_bst(0)
    bst.print_bst(1)
    bst.print_bst(2)
    bst.print_bst(3)

    bst.is_full()

    bst.height()
    bst.height(node2)

    bst.contains(5)

    bst.find_min()
    bst.find_max()

    bst.is_balanced()

    bst.delete(node0)
    bst.print_bst(2)


if __name__ == '__main__':
    main()
