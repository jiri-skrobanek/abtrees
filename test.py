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
        self.assertFalse(tree.contains(1000000))

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


class DeleteFromTree(unittest.TestCase):

    def test_delete(self):
        tree = ABTree(2,3)
        for i in range(50):
            tree.insert((7*i+3) % 101, (7*i+3) % 101)
        tree.delete(7*10+3)

        self.assertEqual(49, tree.item_count())

    def test_empty(self):
        tree = ABTree(3, 5)
        for i in range(50):
            tree.insert((37 * i + 3) % 25999, (37 * i + 3) % 25999)

        for i in range(50):
            tree.delete((37 * i + 3) % 25999)

    def test_empty2(self):
        tree = ABTree(3, 5)
        for i in range(5000):
            tree.insert((37 * i + 3) % 25999, (37 * i + 3) % 25999)

        for i in range(5000):
            tree.delete((37 * i + 3) % 25999)

        self.assertEqual(tree.item_count(), 0)


class Contains(unittest.TestCase):

    def test_all(self):
        tree = ABTree(3, 5)
        values = set()
        for i in range(50):
            value = (37 * i + 3) % 25999
            tree.insert(value, value)
            values.add(value)

        for i in range(0, 25999):
            self.assertEqual(tree.contains(i), i in values)


class Find(unittest.TestCase):

    def test_all(self):
        tree = ABTree(3, 5)
        values = set()
        for i in range(50):
            value = (37 * i + 3) % 25999
            tree.insert(value, value)
            values.add(value)

        for i in range(0, 25999):
            self.assertEqual(tree.find(i), i)
