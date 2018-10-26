import abtree
import unittest


class MakeTree(unittest.TestCase):

    def test_basic(self):
        tree = abtree.ABTree(2,3)
        tree.insert(100,100)
        tree.insert(200,200)
        tree.insert(500,500)
        tree.insert(700,700)
        tree.insert(300,300)
        print(tree.root)
        print(tree.root.children[0])
        print(tree.root.children[1])

    def test_basic_another(self):
        tree = abtree.ABTree(3, 7)
        for i in range(32):
            tree.insert(i, i)
        print(tree.count)

    def test_great(self):
        tree = abtree.ABTree(3, 7)
        for i in range(350):
            tree.insert(i, i)
        print(tree.count)

    def test_23(self):
        tree = abtree.ABTree(2, 3)
        for i in range(100):
            tree.insert(3 * i, 3 * i)

    def test_contains(self):
        tree = abtree.ABTree(2, 3)
        for i in range(100):
            tree.insert(3*i, 3*i)
        self.assertTrue(tree.contains(15))
        self.assertTrue(tree.contains(150))
        self.assertFalse(tree.contains(-7))
        self.assertFalse(tree.contains(1e6))