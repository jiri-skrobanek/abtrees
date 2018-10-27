from abtree import *
import unittest


class MakeTree(unittest.TestCase):

    def test_basic(self):
        tree = ABTree(2,3)
        tree.insert(100,100)
        tree.insert(200,200)
        tree.insert(500,500)
        tree.insert(700,700)
        tree.insert(300,300)
        print(tree.root)
        print(tree.root.children[0])
        print(tree.root.children[1])

    def test_basic_another(self):
        tree = ABTree(3, 7)
        for i in range(32):
            tree.insert(i, i)
        print(tree.count)

    def test_great(self):
        tree = ABTree(3, 7)
        for i in range(350):
            tree.insert(i, i)
        print(tree.count)

    def test_23(self):
        tree = ABTree(2, 3)
        for i in range(100):
            tree.insert(3 * i, 3 * i)

    def test_contains(self):
        tree = ABTree(2, 3)
        for i in range(100):
            tree.insert(3*i, 3*i)
        self.assertTrue(tree.contains(15))
        self.assertTrue(tree.contains(150))
        self.assertFalse(tree.contains(-7))
        self.assertFalse(tree.contains(1e6))

    def test_make_dummy_tree(self):
        tree = ABTree(2, 3)
        tree.root = InternalNode(None)
        tree.level = 2

        left = InternalNode(tree.root)

        one = ExternalNode(1, 1)
        two = ExternalNode(2, 2)
        three = ExternalNode(3, 3)

        left.children = [
            one, two, three
        ]
        left.keys = [
            1, 2, 9999
        ]

        right = InternalNode(tree.root)

        six = ExternalNode(6, 9)
        nine = ExternalNode(9, 9)

        right.children = [
            six, nine
        ]
        right.keys = [
            6, 9999
        ]

        tree.root.children = [
            left, right
        ]
        tree.root.keys = [
            3, 9999
        ]