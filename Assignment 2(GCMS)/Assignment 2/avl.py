from node import Node


def comp_1(node_1, node_2):
    pass


class AVLTree:
    def __init__(self, compare_function=comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, node):

        temp = node.left
        temp2 = temp.right

        temp.right = node
        node.left = temp2

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        temp.height = 1 + max(self.get_height(temp.left), self.get_height(temp.right))
        return temp

    def left_rotate(self, node):

        temp = node.right
        T2 = temp.left

        temp.left = node
        node.right = T2

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        temp.height = 1 + max(self.get_height(temp.left), self.get_height(temp.right))

        return temp

    def insert(self, node, key):

        if not node:
            return Node(key, height=1)

        if node.key[0] > key[0]:
            node.left = self.insert(node.left, key)
        elif node.key[0] < key[0]:
            node.right = self.insert(node.right, key)
        else:
            raise Exception("Same key in avl tree ")

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and key[0] < node.left.key[0]:
            return self.right_rotate(node)

        if balance < -1 and key[0] > node.right.key[0]:
            return self.left_rotate(node)

        if balance > 1 and key[0] > node.left.key[0]:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and key[0] < node.right.key[0]:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def successor(self, node):
        while node.left:
            node = node.left
        return node

    def delet(self, node, key):

        if not node:
            return node

        if key[0] < node.key[0]:
            node.left = self.delet(node.left, key)

        elif key[0] > node.key[0]:
            node.right = self.delet(node.right, key)

        else:
            if (node.right == None) or (node.left == None):
                node = node.right if node.right else node.left

            else:
                succ = self.successor(node.right)
                node.key = succ.key
                node.right = self.delet(node.right, succ.key)

        if not node:
            return None

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def search(self, node, target):

        dummy = node

        while dummy:
            if dummy.key[0] == target:
                return dummy
            elif dummy.key[0] > target:
                dummy = dummy.left
            else:
                dummy = dummy.right
        pass

    def compact_fit(self, node, target, largest=True):

        if node is None:
            return None
        curr = node
        prev = None
        while curr:
            if curr.key[0] >= target:
                if prev == None or curr.key[0] < prev.key[0]:
                    prev = curr
                curr = curr.left
            else:
                curr = curr.right
        if prev is None:
            return None
        if not largest:
            dummy = prev
            if dummy.left is not None:

                while dummy:
                    if dummy.key[0] == prev.key[0]:
                        if dummy.key[1] <= prev.key[1]:
                            prev = dummy
                        dummy = dummy.left
                    else:
                        dummy = dummy.right

            return prev

        else:
            dummy = prev
            if dummy.right:
                while dummy:
                    if dummy.key[0] == prev.key[0]:
                        if dummy.key[1] >= prev.key[1]:
                            prev = dummy
                        dummy = dummy.right
                    else:
                        dummy = dummy.left
            return prev
        pass

    def largest_fit(self, node, target, largest=True):

        if node is None:
            return None
        curr = node
        prev = None

        if curr.right:
            while curr:
                if prev is None or curr.key[0] > prev.key[0]:
                    prev = curr
                curr = curr.right
        else:
            prev = curr

        if prev is None:
            return None
        if prev.key[0] < target:
            return None

        if not largest:
            dummy = prev
            if dummy.left:
                while dummy:
                    if dummy.key[0] == prev.key[0]:
                        if dummy.key[1] <= prev.key[1]:
                            prev = dummy
                        dummy = dummy.left
                    else:
                        dummy = dummy.right
            return prev

        else:
            dummy = prev
            while prev.right:
                prev = prev.right
            return prev
        pass

    def mul_key_insert(self, node, key):
        if not node:
            return Node(key, height=1)

        if (node.key[0], node.key[1]) > (key[0], key[1]):
            node.left = self.mul_key_insert(node.left, key)
        elif (node.key[0], node.key[1]) < (key[0], key[1]):
            node.right = self.mul_key_insert(node.right, key)
        else:
            return None


        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and (key[0], key[1]) < (node.left.key[0], node.left.key[1]):
            return self.right_rotate(node)

        if balance < -1 and (key[0], key[1]) > (node.right.key[0], node.right.key[1]):
            return self.left_rotate(node)

        if balance > 1 and (key[0], key[1]) > (node.left.key[0], node.left.key[1]):
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and (key[0], key[1]) < (node.right.key[0], node.right.key[1]):
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def mul_key_delet(self, node, key):
        if not node:
            return node

        if (key[0], key[1]) < (node.key[0], node.key[1]):
            node.left = self.mul_key_delet(node.left, key)

        elif (key[0], key[1]) > (node.key[0], node.key[1]):
            node.right = self.mul_key_delet(node.right, key)

        else:
            if (node.right == None) or (node.left == None):
                node = node.right if node.right else node.left

            else:
                succ = self.successor(node.right)
                node.key = succ.key
                node.right = self.mul_key_delet(node.right, succ.key)

        if not node:
            return None

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node
