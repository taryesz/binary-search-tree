# Binary Search Tree

This repository contains a binary search tree implementation using Python and OOP principles. All classes are in
separate files (modules).

# Testing

* To create a node, use:
```python
your_name = Node()
```
* To give this node a value, use:
```python
your_name.set_value(some_value)
```
* To create a tree, use:
```python
bst = BinarySearchTree()
```
* To add this node to a tree, use:
```python
bst.insert(your_node)
```
* To delete a node, use:
```python
bst.delete(your_node)
```
* To print the contents of the tree, use:
```python
bst.print_bst()
```
* To check if the tree is full, use:
```python
bst.is_full()
```
* To get the tree height, use:
```python
bst.height()
```
If you want to get a subtree height, starting from a custom node, use:
```python
bst.height(your_node)
```
* To check if a value is in the tree, use:
```python
bst.contains(your_value)
```
* To get the smallest value, use:
```python
bst.find_min()
```
* To get the biggest value, use:
```python
bst.find_max()
```
* To check if the tree is balanced, use:
```python
bst.is_balanced()
```