import random


class BinarySearchTree:

    def __init__(self):
        self.__root = None

    def insert(self, insert_node, starting_node=0) -> None:

        # if there is no root, it means that the tree is empty
        # our node becomes the root

        if self.__root is None:
            self.__root = insert_node
            print(f"Successfully inserted a node as the root (value: {insert_node.get_value()}).")
        else:

            # now we need to check our starting point AKA a node we consider a root of a (sub)tree
            # if we put the 2nd argument (starting_node) to our insert() function when calling it
            # then this argument (node) will be the root of a subtree
            # else, if we don't specify this node, then the root of the whole BST is used

            bst_node = None

            if starting_node == 0:
                bst_node = self.__root
            else:
                bst_node = starting_node

            # now check the values:

            # if insert_node's value is smaller than the current root's one,
            # then check if this root has a left child
            # if yes, call insert() again with this root's left child as the starting point
            # else, assign this node as this root's left child (insert)

            # the same logic the opposite case

            # if the values are same, don't bother and just don't add anything

            # finally, 'else:' case is for unexpected behaviour

            if insert_node.get_value() < bst_node.get_value():
                if bst_node.get_left():
                    self.insert(insert_node, bst_node.get_left())
                else:
                    bst_node.set_left(insert_node)
                    print(f"Successfully inserted a node (value: {insert_node.get_value()}).")
            elif insert_node.get_value() > bst_node.get_value():
                if bst_node.get_right():
                    self.insert(insert_node, bst_node.get_right())
                else:
                    bst_node.set_right(insert_node)
                    print(f"Successfully inserted a node (value: {insert_node.get_value()}).")
            elif insert_node.get_value() == bst_node.get_value():
                print(f"\n>>> Warning: You're trying to insert a duplicate (value: {insert_node.get_value()}). "
                      f"This node will not be added. <<<\n")
            else:
                print("Ouch! Something went wrong.")

    @staticmethod
    def __replacement_process(node_to_delete, bst_node, left_subtree, what_to_set) -> None:

        if left_subtree:
            bst_node.set_left(what_to_set)
        else:
            bst_node.set_right(what_to_set)

    def __check_node_to_delete_type(self, node_to_delete, bst_node, direction_of_further_movement) -> None:

        # if the node is a leaf
        if node_to_delete.get_left() is None and node_to_delete.get_right() is None:
            if direction_of_further_movement is None:   # if the node_to_delete is the root
                self.__root = None
            else:
                self.__replacement_process(node_to_delete, bst_node, direction_of_further_movement, None)
            del node_to_delete

        # if the node has a left child -> replace the node with this left child
        elif node_to_delete.get_left() is not None and node_to_delete.get_right() is None:
            left_child = node_to_delete.get_left()
            if direction_of_further_movement is None:
                self.__root = left_child
            else:
                self.__replacement_process(node_to_delete, bst_node, direction_of_further_movement, left_child)
            del node_to_delete

        # if the node has a right child -> replace the node with this right child
        elif node_to_delete.get_right() is not None and node_to_delete.get_left() is None:
            right_child = node_to_delete.get_right()
            if direction_of_further_movement is None:
                self.__root = right_child
            else:
                self.__replacement_process(node_to_delete, bst_node, direction_of_further_movement, right_child)
            del node_to_delete

        # if the node has both children -> replace the node with either its predecessor or successor (random choice)
        elif node_to_delete.get_left() is not None and node_to_delete.get_right() is not None:

            # since this case is when we randomly choose what node to replace the deleted one with
            # we will use a generator of boolean values to decide which one to use

            type_of_replacement = None

            if random.choice([True, False]):
                type_of_replacement = True
            else:
                type_of_replacement = False

            # ------------------------------------------------------------------------------------------

            if type_of_replacement:
                # if True, then look for a successor
                successor = self.__find_successor(node_to_delete)
                if direction_of_further_movement is None:
                    self.__root = successor
                else:
                    self.__replacement_process(node_to_delete, bst_node, direction_of_further_movement, successor)
                del node_to_delete
            else:
                # if False, then look for a predecessor
                predecessor = self.__find_predecessor(node_to_delete)
                if direction_of_further_movement is None:
                    # bst_node = predecessor
                    self.__root = predecessor
                else:
                    self.__replacement_process(node_to_delete, bst_node, direction_of_further_movement, predecessor)
                del node_to_delete

    def __find_predecessor(self, node_to_delete):

        flag = False
        left_child = node_to_delete.get_left()
        predecessor = None
        parent_of_predecessor = None

        if left_child.get_right() is not None:
            parent_of_predecessor = left_child
            predecessor = left_child.get_right()
            while True:
                if predecessor.get_right() is None:
                    parent_of_predecessor.set_right(None)
                    self.__check_node_to_delete_type(predecessor, parent_of_predecessor, False)
                    break
                else:
                    parent_of_predecessor = predecessor
                    predecessor = predecessor.get_right()
        else:
            flag = True
            parent_of_predecessor = node_to_delete
            predecessor = left_child

        right_child = node_to_delete.get_right()
        predecessor.set_right(right_child)

        if not flag:
            predecessor.set_left(left_child)

        return predecessor

    def __find_successor(self, node_to_delete):

        flag = False
        right_child = node_to_delete.get_right()
        successor = None
        parent_of_successor = None

        if right_child.get_left() is not None:
            parent_of_successor = right_child
            successor = right_child.get_left()
            while True:
                if successor.get_left() is None:
                    parent_of_successor.set_left(None)
                    self.__check_node_to_delete_type(successor, parent_of_successor, True)
                    break
                else:
                    parent_of_successor = successor
                    successor = successor.get_left()
        else:
            flag = True
            parent_of_successor = node_to_delete
            successor = right_child

        left_child = node_to_delete.get_left()
        successor.set_left(left_child)

        # if the successor of the node we want to delete is its direct child, then ...
        if not flag:
            successor.set_right(right_child)

        return successor

    def delete(self, node_to_delete, starting_node=0, recursion=False) -> None:

        error = False
        value = node_to_delete.get_value()

        if self.__root is None:
            print(f"Nothing to delete. The tree is empty.")
        else:

            bst_node = None

            if starting_node == 0:
                bst_node = self.__root
            else:
                bst_node = starting_node

            if node_to_delete.get_value() < bst_node.get_value():
                if bst_node.get_left().get_value() == node_to_delete.get_value():
                    self.__check_node_to_delete_type(node_to_delete, bst_node, True)
                else:
                    self.delete(node_to_delete, bst_node.get_left(), True)
            elif node_to_delete.get_value() > bst_node.get_value():
                if bst_node.get_right().get_value() == node_to_delete.get_value():
                    self.__check_node_to_delete_type(node_to_delete, bst_node, False)
                else:
                    self.delete(node_to_delete, bst_node.get_right(), True)
            elif node_to_delete.get_value() == bst_node.get_value():

                # pass
                # when the node we want to delete is actually the root of the whole tree
                self.__check_node_to_delete_type(node_to_delete, bst_node, None)

            else:
                error = True
                print("Ouch! Something went wrong.")

        if not recursion:
            if not error:
                print("\n\n--------------------------------------------------------------------------------"
                      "---------------")
                print(f"\n\nSuccessfully deleted node {value}.")

    def print_bst(self, recursion=False, starting_node=0) -> None:

        if not recursion:
            print("\n\n^ The tree after this operation:\n\n")
            self.get_root()

        bst_node = None

        if starting_node == 0:
            bst_node = self.__root
        else:
            bst_node = starting_node

        if self.__root is None:
            print("Nothing to print. The tree is empty")
        else:
            if bst_node.get_left():
                self.print_bst(True, bst_node.get_left())
            print(f"Node: {bst_node.get_value()}. Its children are: "
                  f"Left = {str(bst_node.get_left().get_value() if bst_node.get_left() else None)}, "
                  f"Right = {str(bst_node.get_right().get_value() if bst_node.get_right() else None)}")
            if bst_node.get_right():
                self.print_bst(True, bst_node.get_right())

    def get_root(self):
        print(f">>> Root: {self.__root.get_value() if self.__root else None} <<<\n")
