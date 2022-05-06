import unittest

from unrolled_linked_list import UnrolledLinkedList


def is_even(x):
    return x % 2 == 0


def is_odd(x):
    return x % 2 == 1


class unrolled_linked_list_test(unittest.TestCase):
    def test_default_node_capacity(self):
        L = UnrolledLinkedList()
        self.assertEqual(L.max_node_capacity, 4)

    def test_custom_node_capacity(self):
        L = UnrolledLinkedList(4)
        self.assertEqual(L.max_node_capacity, 4)

        L = UnrolledLinkedList(15)
        self.assertEqual(L.max_node_capacity, 15)

    def test_empty(self):
        L = UnrolledLinkedList()
        self.assertEqual(str(L), "{}")
        L.append(1)
        del L[0]
        self.assertEqual(str(L), "{}")

    def test_delete_item(self):
        L = UnrolledLinkedList()
        L.append(1)
        L.append(2)
        L.append(3)
        del L[1]
        self.assertEqual(str(L), '{[1, 3]}')

    def test_get_item(self):
        L = UnrolledLinkedList()
        L.append(2)
        L.append(3)
        self.assertEqual(L.__getitem__(1), 3)
        self.assertEqual(str(L[0]), '2')

    def test_set_item(self):
        L = UnrolledLinkedList()
        L.append(1)
        L.append(2)
        L.append(3)
        L[1] = 42
        self.assertEqual(str(L[1]), '42')

    def test_iteration(self):
        L = UnrolledLinkedList()
        L.append(1)
        L.append(2)
        L.append(3)
        arr = []
        for i in L:
            arr.append(i)

        self.assertEqual(arr[0], L[0])
        self.assertEqual(arr[1], L[1])
        self.assertEqual(arr[2], L[2])

    def test_len(self):
        L = UnrolledLinkedList()
        L.append(1)
        L.append(2)
        L.append(3)

        self.assertEqual(str(len(L)), '3')

        L.append(4)

        self.assertEqual(str(len(L)), '4')

    def test_reverse(self):
        testL = [3, 2, 1]
        L = UnrolledLinkedList()
        L.append(1)
        L.append(2)
        L.append(3)

        newL = []

        for x in reversed(L):
            newL.append(x)
        self.assertEqual(newL, testL)

    def test_member(self):
        L = UnrolledLinkedList()
        L.append(1)
        L.append(2)
        L.append(3)
        L.append(4)
        L.append(5)
        L.append(6)
        L.append(7)
        L.append(8)

        self.assertEqual(1 in L, True)
        self.assertEqual(42 in L, False)
        self.assertEqual(8 in L, True)

    def test_variable(self):
        L = UnrolledLinkedList()
        L.append(1)
        L.append(3)
        L.append(4)
        L.append(5)
        L.append(1)
        L.append(7)
        L.append(8)
        self.assertEqual(str(L), '{[1, 3], [4, 5], [1, 7, 8]}')

    def test_to_list(self):
        L = UnrolledLinkedList()
        L.append(1)
        L.append(2)
        L.append(3)
        L.append(4)
        self.assertEqual(str(L.to_list()), '[1, 2, 3, 4]')

    def test_from_list(self):
        list1 = [1, 2, 3]
        L = UnrolledLinkedList()
        self.assertEqual(str(L.from_list(list1)), '{[1, 2, 3]}')

    def test_filter(self):
        L = UnrolledLinkedList()
        L.append(1)
        L.append(2)
        L.append(3)
        self.assertEqual(str(L.filter(is_even)), '{[2]}')
        self.assertEqual(str(L.filter(is_odd)),'{[1, 3]}')

    def test_concat(self):
        L1 = UnrolledLinkedList()
        L1.append(1)
        L1.append(9)
        L2 = UnrolledLinkedList()
        L2.append(5)
        L2.append(3)
        self.assertEqual(str(L1.concat(L2)),'{[1, 3, 5, 9]}')

