import abtree

tree = abtree.ABTree(2, 3)  # Create an empty tree, a = 2, b = 3

# Fill tree with entries:
tree.insert(10, 7), tree.insert(20, 2), tree.insert(0, 3)
tree.insert(30, 5), tree.insert(40, 1), tree.insert(50, 4)

# Remove an entry from the tree:
tree.delete(30)

print("Value at 10: " + str(tree[10]))
print("\nElement greater than 20: " + str(tree.find_greater(20)))
print("\nAmount of entries in the tree: " + str(len(tree)))
