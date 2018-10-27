import math


class InternalNode:
    def __init__(self, parent=None):
        self.keys = []
        self.children = []
        self.parent = parent

    def __str__(self):
        return self.keys.__str__()


class ExternalNode:
    def __init__(self, key: int, value=None):
        self.key = key
        self.value = value


class ABTree:
    def __init__(self, a: int, b: int):
        if a < 2:
            raise ValueError('Improper a,b choice.')
        if b < 2*a - 1:
            raise ValueError('Improper a,b choice.')
        self.a = a
        self.b = b
        self.root = None
        self.level = 0
        self.count = 0

    def item_count(self):
        return self.count

    def find(self, key: int):
        if not self.root:
            return None

        lev = 0
        node = self.root
        while lev < self.level:
            i = 0
            while node.keys[i] < key:
                i += 1

            lev += 1
            node = node.children[i]

        if node.key == key:
            return node.value
        return None

    def insert(self, key: int, value=None):
        if self.root is None:
            self.root = InternalNode(None)
            self.root.keys.append(key)
            self.root.keys.append(math.inf)
            self.root.children.append(ExternalNode(key, value))
            self.root.children.append(ExternalNode(math.inf, None))
            self.level = 1
            self.count = 1
            return

        node = self.root
        for lev in range(self.level - 1):
            i = 0
            while node.keys[i] < key:
                i += 1

            node = node.children[i]

        i = 0
        while node.keys[i] < key:
            i += 1
        if node.keys[i] == key:
            raise ValueError('Repeating key')
        node.keys.insert(i, key)
        node.children.insert(i, ExternalNode(key, value))
        self.__rebalance(node)

        self.count += 1

    def __rebalance(self, node: InternalNode):
        children = len(node.children)

        if node.parent is None:
            if children < 2:
                if isinstance(node.children[0], ExternalNode):
                    self.root = None
                    del node.children[0]
                    del node
                    self.level = 0
                else:
                    self.root = node.children[0]
                    self.root.parent = None
                    del node
                    self.level -= 1
            elif children > self.b:
                lsize = (children + 1) // 2
                left = InternalNode(node)
                left.children = node.children[:lsize]
                for child in left.children:
                    child.parent = left
                left.keys = node.keys[:lsize]
                right = InternalNode(node)
                right.children = node.children[-lsize:]
                for child in right.children:
                    child.parent = right
                right.keys = node.keys[-lsize:]
                self.level += 1
                node.children = [left, right]
                node.keys = [left.keys[-1], right.keys[-1]]
        elif children > self.b:
            lsize = (children + 1) // 2
            new_node = InternalNode(node.parent)
            new_node.children = node.children[:lsize]
            for child in new_node.children:
                child.parent = new_node
            new_node.keys = node.keys[:lsize]
            node.children = node.children[-lsize:]
            node.keys = node.keys[-lsize:]
            new_key = new_node.keys[-1]
            i = 0
            while node.parent.keys[i] < new_key:
                i += 1
            node.parent.keys.insert(i, new_key)
            node.parent.children.insert(i, new_node)
            self.__rebalance(node.parent)
        elif children < self.a:
            i = 0
            while node.parent.keys[i] < node.keys[-1]:
                i += 1
            if i < len(node.parent.keys) - 1 and len(node.parent.children[i+1].keys) == self.a:
                self.__fuse_ith_with_right(node.parent, i)
            elif i < 0 and len(node.parent.children[i-1].keys) == self.a:
                self.__fuse_ith_with_right(node.parent, i - 1)
            elif i < len(node.parent.keys) - 1:
                self.__fuse_ith_with_right(node.parent, i)
            else:
                self.__fuse_ith_with_right(node.parent, i - 1)

    def __fuse_ith_with_right(self, node: InternalNode, i: int):
        left = node.children[i]
        right = node.children[i+1]
        right.keys = left.keys + right.keys
        right.children = left.children + right.children
        del node.children[i]
        del node.keys[i]
        for child in right.children:
            child.parent = right
        self.__rebalance(right)

    def find_leq(self, key: int):
        if key == math.inf:
            raise ValueError('Infinity!')
        if self.root is None:
            return None

        node = self.root
        for lev in range(self.level - 1):
            i = 0
            while i < len(node.keys) - 1 and node.keys[i+1] <= key:
                i += 1
            node = node.children[i]

        i = 0
        while i < len(node.keys) - 1 and node.keys[i + 1] < key:
            i += 1
        return node.children[i].key, node.children[i].value

    def find_lesser(self, key: int):
        if key == math.inf:
            raise ValueError('Infinity!')
        if self.root is None:
            return None

        node = self.root
        for lev in range(self.level - 1):
            i = 0
            while i < len(node.keys) - 1 and node.keys[i + 1] < key:
                i += 1
            node = node.children[i]

        i = 0
        while i < len(node.keys) - 1 and node.keys[i + 1] < key:
            i += 1
        return node.children[i].key, node.children[i].value

    def find_geq(self, key: int):
        if key == math.inf:
            raise ValueError('Infinity!')
        if self.root is None:
            return None

        node = self.root
        for lev in range(self.level - 1):
            i = 0
            while node.keys[i] < key:
                i += 1
            node = node.children[i]

        i = 0
        while node.keys[i] < key:
            i += 1
        return node.children[i].key, node.children[i].value

    def find_greater(self, key: int):
        if key == math.inf:
            raise ValueError('Infinity!')
        if self.root is None:
            return None

        node = self.root
        for lev in range(self.level - 1):
            i = 0
            while node.keys[i] <= key:
                i += 1
            node = node.children[i]

        i = 0
        while node.keys[i] <= key:
            i += 1
        return node.children[i].key, node.children[i].value

    def contains(self, key: int):
        node = self.root
        lvl = 0

        node = self.root
        while lvl < self.level:
            i = 0
            while node.keys[i] < key:
                i += 1

            if node.keys[i] == key:
                return True
            lvl += 1
            node = node.children[i]

        return False

    def delete(self, key: int):
        if not self.root:
            raise ValueError('No such key in tree.')

        lev = 0
        node = self.root
        while lev < self.level - 1:
            i = 0
            while node.keys[i] < key:
                i += 1

            lev += 1
            node = node.children[i]

        i = 0
        while node.keys[i] < key:
            i += 1

        if node.keys[i] != key:
            raise ValueError('No such key in tree.')

        del node.children[i]
        del node.keys[i]

        if i == len(node.keys): # Deleted last key, change keys in ancestors.
            parent = node.parent
            while lev >= 0:
                j = 0
                while parent.keys[j] < key:
                    j += 1

                if parent.keys[j] == key:
                    parent.keys[j] = node.keys[i-1]
                else:
                    break

                lev -= 1
                parent = parent.parent

        self.__rebalance(node)

        self.count -= 1