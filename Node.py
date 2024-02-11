class Node:

    def __init__(self):
        self.__value = None
        self.__left = None
        self.__right = None

    def set_value(self, value) -> None:
        self.__value = value

    def set_left(self, left_node) -> None:
        self.__left = left_node

    def set_right(self, right_node) -> None:
        self.__right = right_node

    def get_value(self):
        return self.__value

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right