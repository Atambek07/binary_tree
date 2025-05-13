"""
Binary Search Tree Implementation in Python
This script demonstrates a simple implementation of a Binary Search Tree (BST) with basic operations like:
- Insertion
- Search
- Deletion
- In-order Traversal
- Check if the tree is empty

A Binary Search Tree (BST) is a tree data structure where each node has at most two children (left and right). 
For every node, all elements in the left subtree are smaller, and all elements in the right subtree are larger than the node itself.

Time Complexity:
- Insertion, Search, and Deletion: O(log n) in average case (balanced tree), O(n) in worst case (unbalanced tree).
- In-order Traversal: O(n), where n is the number of nodes in the tree.
Space Complexity: O(n) for the tree structure.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.value == key:
            return node

        if key < node.value:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node

        if key < node.value:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.value:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.value = self._min_value_node(node.right).value
            node.right = self._delete_recursive(node.right, node.value)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def is_empty(self):
        return self.root is None


if __name__ == "__main__":
    bst = BinarySearchTree()

    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print("In-order traversal:", bst.inorder_traversal())

    key = 40
    result = bst.search(key)
    if result:
        print(f"Node with value {key} found.")
    else:
        print(f"Node with value {key} not found.")

    bst.delete(20)
    print("In-order traversal after deletion of 20:", bst.inorder_traversal())

    print("Is the tree empty?", bst.is_empty())

    bst.delete(30)
    bst.delete(40)
    bst.delete(50)
    bst.delete(70)
    bst.delete(60)
    bst.delete(80)
    print("Is the tree empty after deleting all nodes?", bst.is_empty())
