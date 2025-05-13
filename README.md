# Binary Search Tree (BST) Implementation in Python

This repository contains a simple implementation of a **Binary Search Tree (BST)** in Python. The tree includes basic operations such as:

- **Insertion**: Adds a node to the tree.
- **Search**: Searches for a value in the tree.
- **Deletion**: Deletes a node from the tree.
- **In-order Traversal**: Traverses the tree in sorted order.
- **Check if Tree is Empty**: Checks if the tree has no nodes.

## Binary Search Tree (BST)

A Binary Search Tree (BST) is a tree data structure where each node has at most two children. For every node:

- The left child contains values smaller than the node.
- The right child contains values larger than the node.

### Features

- **Insertion**: Inserts a new node at the correct position based on its value.
- **Search**: Searches for a given value in the tree.
- **Deletion**: Removes a node. Handles cases for nodes with zero, one, or two children.
- **In-order Traversal**: Returns the values of the nodes in ascending order.
- **Empty Check**: Checks if the tree is empty (no nodes).

### Time and Space Complexity

- **Insertion, Search, Deletion**: 
   - O(log n) in average case (balanced tree).
   - O(n) in the worst case (unbalanced tree).
- **In-order Traversal**: O(n), where `n` is the number of nodes in the tree.
- **Space Complexity**: O(n) for the tree structure.

## Requirements
- Python 3.x

## Installation

**1. Clone the repository:**
```bash
git clone https://github.com/your-username/binary-search-tree-python.git
```

**2. Navigate to the project directory:**
```bash
cd binary-search-tree-python
```

**3. Run the script:**
```bash
python binary_tree.py
```
