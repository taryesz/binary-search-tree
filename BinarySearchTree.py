import random
from typing import Union
from Node import Node

class BinarySearchTree:

    def __init__(self):
        self.__is_full = True
        self.__root = None
        self.__heights = {}

    def insert(self, insert_node, starting_node=0) -> None:

        # if there is no root, it means that the tree is empty
        # our node becomes the root

        if self.__root is None:
            self.__root = insert_node
            print(f"Successfully inserted a node as the root {insert_node.get_value()}")
        else:

            # now we need to check our starting point AKA a node we consider a root of a (sub)tree
            # if we put the 2nd argument (starting_node) to our insert() function when calling it
            # then this argument (node) will be the root of a subtree
            # else, if we don't specify this node, then the root of the whole BST is used

            bst_node = self.__find_local_root(starting_node)

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
                    print(f"Successfully inserted a node {insert_node.get_value()}")
            elif insert_node.get_value() > bst_node.get_value():
                if bst_node.get_right():
                    self.insert(insert_node, bst_node.get_right())
                else:
                    bst_node.set_right(insert_node)
                    print(f"Successfully inserted a node {insert_node.get_value()}")
            elif insert_node.get_value() == bst_node.get_value():
                print(f"Warning: You're trying to insert a duplicate ({insert_node.get_value()}). "
                      f"This node will not be added")
            else:
                print("Ouch! Something went wrong")

    @staticmethod
    def __replacement_process(bst_node, left_subtree, what_to_set) -> None:

        """

        :param bst_node: A parent node of the node we will delete from the tree.
        :param left_subtree: A boolean value that decides which subtree will we move to.
        :param what_to_set: A node, that will be used to replace 'node_to_delete'.
        :return: This function won't return anything.

        This function replaces the node's parent's child to the node's replacement.
        """

        if left_subtree:
            bst_node.set_left(what_to_set)
        else:
            bst_node.set_right(what_to_set)

    def __check_if_root(self, direction_of_further_movement, node_to_delete, bst_node, replacement=None) -> None:

        """

        :param direction_of_further_movement: A boolean value that decides which subtree will we move to.
        :param node_to_delete: A node, that we will delete from the tree.
        :param bst_node: A parent node of the node we will delete from the tree.
        :param replacement: A node, that will be used to replace 'node_to_delete'.
        :return: This function won't return anything.

        This function checks if the node (we want to delete) is the root of the tree:

        1) If the 'direction_of_further_movement':
            - it means that the node we are trying to delete is the root of the tree;
            - replace the current root with its replacement (successor or predecessor).
        2) Else, call __replacement_process() that will set the node's parent's new child.
        3) Delete the node.
        """

        if direction_of_further_movement is None:
            self.__root = replacement
        else:
            self.__replacement_process(bst_node, direction_of_further_movement, replacement)

        del node_to_delete

    @staticmethod
    def __random_choice_generator() -> bool:

        """

        :return: This function will return a boolean value.

        This function generates a random boolean value, needed to randomly choose a replacement node: successor or
        predecessor.
        """

        if random.choice([True, False]):
            type_of_replacement = True
        else:
            type_of_replacement = False

        return type_of_replacement

    def __check_node_to_delete_type(self, node_to_delete, bst_node, direction_of_further_movement) -> None:

        """

        :param node_to_delete: A node, that we will delete from the tree.
        :param bst_node: A parent node of the node we will delete from the tree.
        :param direction_of_further_movement: A boolean value that decides which subtree will we move to.
        :return: This function won't return anything.

        This function checks if the node (we want to delete) has any children:

        1) If the node is a leaf itself, then check if it's not a root of the tree, delete it and update its parent.
        2) If the node has a left child, then replace this node with its left child.
        3) If the node has a right child, then replace this node with its right child.
        4) If the node has both children, then replace the node with either its predecessor or a successor (randomly):
            - since we choose a replacement randomly, a __random_choice_generator() was introduced;
            - if __random_choice_generator() returns 'True', then the node will be replaced with a successor;
            - if __random_choice_generator() returns 'False', then the node will be replaced with a predecessor.

        The following logic implementation is executed in __replacement_process(),
        which is called from the inside of __check_if_root().
        """

        if node_to_delete.get_left() is None and node_to_delete.get_right() is None:
            self.__check_if_root(direction_of_further_movement, node_to_delete, bst_node)
        elif node_to_delete.get_left() is not None and node_to_delete.get_right() is None:
            left_child = node_to_delete.get_left()
            self.__check_if_root(direction_of_further_movement, node_to_delete, bst_node, left_child)
        elif node_to_delete.get_right() is not None and node_to_delete.get_left() is None:
            right_child = node_to_delete.get_right()
            self.__check_if_root(direction_of_further_movement, node_to_delete, bst_node, right_child)
        elif node_to_delete.get_left() is not None and node_to_delete.get_right() is not None:

            type_of_replacement = self.__random_choice_generator()

            if type_of_replacement:
                successor = self.__find_successor(node_to_delete)
                self.__check_if_root(direction_of_further_movement, node_to_delete, bst_node, successor)
            else:
                predecessor = self.__find_predecessor(node_to_delete)
                self.__check_if_root(direction_of_further_movement, node_to_delete, bst_node, predecessor)

    def __find_predecessor(self, node_to_delete) -> Node:

        """

        :param node_to_delete: A node, that we will delete from the tree.
        :return: This function will return a predecessor (of type Node).

        This function finds a predecessor of 'node_to_delete'.

        1) If a left child of 'node_to_delete' has a right child:
            - iterate to the right as many times as there are the right subtrees.
            - then, save and delete this right-most node.
        2) Else, the predecessor is the left child of 'node_to_delete'.
        3) Return the predecessor.
        """

        flag = False
        left_child = node_to_delete.get_left()

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
            predecessor = left_child

        right_child = node_to_delete.get_right()
        predecessor.set_right(right_child)

        if not flag:
            predecessor.set_left(left_child)

        return predecessor

    def __find_successor(self, node_to_delete) -> Node:

        """

        :param node_to_delete: A node, that we will delete from the tree.
        :return: This function will return a successor (of type Node).

        This function finds a successor of 'node_to_delete'.

        1) If a right child of 'node_to_delete' has a left child:
            - iterate to the left as many times as there are the left subtrees.
            - then, save and delete this left-most node.
        2) Else, the successor is the right child of 'node_to_delete'.
        3) Return the successor.
        """

        flag = False
        right_child = node_to_delete.get_right()

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
            successor = right_child

        left_child = node_to_delete.get_left()
        successor.set_left(left_child)

        if not flag:
            successor.set_right(right_child)

        return successor

    def delete(self, node_to_delete, starting_node=0, recursion=False) -> None:

        error = False
        value = node_to_delete.get_value()

        if self.__root is None:
            print(f"Nothing to delete. The tree is empty.")
        else:

            bst_node = self.__find_local_root(starting_node)

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
                self.__check_node_to_delete_type(node_to_delete, bst_node, None)
            else:
                error = True
                print("Ouch! Something went wrong.")

        if not recursion:
            if not error:
                print(f"Successfully deleted node {value}.")

    def __choose_method_of_traverse(self, method, starting_node) -> None:

        if starting_node == 0:
            starting_node = self.__root

        self.__heights = {}

        if method == 0:  # breadth-first
            self.__traverse_bfs(starting_node)

        if method == 1:  # depth-first in-order
            self.__traverse_dfs_in_order(starting_node)

        if method == 2:  # depth-first pre-order
            self.__traverse_dfs_pre_order(starting_node)

        if method == 3:  # depth-first post-order
            self.__traverse_dfs_post_order(starting_node)

    def print_bst(self, method) -> None:

        if self.__root is None:
            print("Nothing to print. The tree is empty")
            return

        self.__choose_method_of_traverse(method, 0)

        for node in self.__heights.keys():
            print(f"Node: {node.get_value()}. Its children are: "
                  f"Left = {str(node.get_left().get_value() if node.get_left() else None)}, "
                  f"Right = {str(node.get_right().get_value() if node.get_right() else None)}")

    def __traverse_bfs(self, starting_node=0, distance_counter=0) -> None:

        queue = []
        bst_node = self.__find_local_root(starting_node)

        queue.append(bst_node)
        siblings_counter = -1

        while queue:
            popped = queue.pop(0)
            self.__heights[popped] = distance_counter

            if siblings_counter == -1:
                siblings_counter = 0
                distance_counter = 1

            if siblings_counter == 2:
                siblings_counter = 0
                distance_counter += 1

            if popped.get_left():
                queue.append(popped.get_left())

            if popped.get_right():
                queue.append(popped.get_right())

            siblings_counter += 1

    def __traverse_dfs_in_order(self, starting_node=0, counter=0) -> None:

        bst_node = self.__find_local_root(starting_node)

        counter += 1

        if bst_node.get_left():
            self.__traverse_dfs_in_order(bst_node.get_left(), counter)

        self.__heights[bst_node] = counter  # "in" because IN BETWEEN recursions

        if bst_node.get_right():
            self.__traverse_dfs_in_order(bst_node.get_right(), counter)

    def __traverse_dfs_pre_order(self, starting_node=0, counter=0) -> None:

        bst_node = self.__find_local_root(starting_node)

        counter += 1

        self.__heights[bst_node] = counter  # "pre" because BEFORE recursion

        if bst_node.get_left():
            self.__traverse_dfs_pre_order(bst_node.get_left(), counter)

        if bst_node.get_right():
            self.__traverse_dfs_pre_order(bst_node.get_right(), counter)

    def __traverse_dfs_post_order(self, starting_node=0, counter=0) -> None:

        bst_node = self.__find_local_root(starting_node)

        counter += 1

        if bst_node.get_left():
            self.__traverse_dfs_post_order(bst_node.get_left(), counter)

        if bst_node.get_right():
            self.__traverse_dfs_post_order(bst_node.get_right(), counter)

        self.__heights[bst_node] = counter  # "post" because AFTER recursion

    def contains(self, node, starting_node=0) -> bool:

        bst_node = self.__find_local_root(starting_node)

        if self.__root is None:
            print("Nothing to be found. The tree is empty")
            return False

        if bst_node.get_value() == node:
            return True

        if bst_node.get_left() and self.contains(node, bst_node.get_left()):
            return True

        if bst_node.get_right() and self.contains(node, bst_node.get_right()):
            return True

        return False

    def find_min(self, starting_node=0) -> Union[int, None]:

        bst_node = self.__find_local_root(starting_node)

        if self.__root is None:
            print("Nothing to be found. The tree is empty")
            return False

        if not bst_node.get_left().get_left():
            return bst_node.get_left().get_value()
        else:
            self.find_min(bst_node.get_left())

        return None

    def find_max(self, starting_node=0) -> Union[int, None]:

        bst_node = self.__find_local_root(starting_node)

        if self.__root is None:
            print("Nothing to be found. The tree is empty")
            return False

        if not bst_node.get_right().get_right():
            return bst_node.get_right().get_value()
        else:
            self.find_max(bst_node.get_right())

        return None

    def __find_local_root(self, starting_node) -> Node:

        if starting_node == 0:
            bst_node = self.__root
        else:
            bst_node = starting_node

        return bst_node

    def __create_node_dictionary(self, starting_node=0) -> None:

        self.__heights = {}

        method = random.randint(1, 3)  # TODO: change 1 to 0 after BFS implemented
        self.__choose_method_of_traverse(method, starting_node)

    def is_full(self) -> bool:

        self.__create_node_dictionary()

        for node in self.__heights.keys():
            if self.__is_full is True:
                self.__is_full = True if (node.get_left() and node.get_right()) or \
                                (not node.get_left() and not node.get_right()) else False

        return self.__is_full

    def height(self, starting_node=0) -> int:

        self.__create_node_dictionary(starting_node)

        height = 0
        for i in self.__heights.values():
            if i > height:
                height = i

        return height

    def is_balanced(self) -> bool:

        if not self.__root:
            print("The tree is empty. Cannot check if balanced")
            return False

        self.__create_node_dictionary()

        dictionary = self.__heights

        for node in dictionary.keys():

            if node.get_left() and node.get_right():
                left_subtree_height = self.height(node.get_left())
                right_subtree_height = self.height(node.get_right())

                if abs(left_subtree_height - right_subtree_height) > 1:
                    return False

            elif node.get_left() and not node.get_right():
                left_subtree_height = self.height(node.get_left())
                right_subtree_height = 0

                if abs(left_subtree_height - right_subtree_height) > 1:
                    return False

            elif node.get_right() and not node.get_left():
                left_subtree_height = 0
                right_subtree_height = self.height(node.get_right())

                if abs(left_subtree_height - right_subtree_height) > 1:
                    return False

        return True
