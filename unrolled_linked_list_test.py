import unittest

import hypothesis.strategies as st
from hypothesis import given, settings

from unrolled_linked_list import UnrolledLinkedList


def is_even(x: int) -> bool:
    return x % 2 == 0


def is_odd(x: int) -> bool:
    return x % 2 == 1


def _sum(state, x: list):
    for i in range(len(x)):
        state += x[i]
    return state


class unrolled_linked_list_test(unittest.TestCase):
    def test_default_node_capacity(self):
        L = UnrolledLinkedList()
        self.assertEqual(L.max_node_capacity, 4)

    # PBT test
    @settings(max_examples=10)
    @given(a=st.integers(), b=st.integers())
    def test_custom_node_capacity(self, a, b):
        L = UnrolledLinkedList(a)
        self.assertEqual(L.max_node_capacity, a)

        L = UnrolledLinkedList(b)
        self.assertEqual(L.max_node_capacity, b)

    # PBT test
    @settings(max_examples=10)
    @given(a=st.integers())
    def test_empty(self, a):
        L = UnrolledLinkedList()
        self.assertEqual(str(L), "{}")
        L.append(a)
        del L[0]
        self.assertEqual(str(L), "{}")

    # PBT test
    @settings(max_examples=10)
    @given(a=st.integers(), b=st.integers(), c=st.integers())
    def test_delete_item(self, a, b, c):
        L = UnrolledLinkedList().append(a).append(b).append(c)
        del L[0]
        del L[1]
        L2 = UnrolledLinkedList().append(c).append(b).append(a)
        del L2[0]
        del L2[1]
        self.assertEqual(str(L), '{[%d]}' % b)
        self.assertEqual(str(L2) == str(L), True)

    # PBT test
    @settings(max_examples=10)
    @given(a=st.integers(), b=st.integers())
    def test_get_item(self, a, b):
        L = UnrolledLinkedList()
        L.append(a).append(b)
        self.assertEqual(L.__getitem__(1), b)
        self.assertEqual(str(L[0]), '%d' % a)

    # PBT test
    @settings(max_examples=10)
    @given(a=st.integers(), b=st.integers(), c=st.integers())
    def test_set_item(self, a, b, c):
        L = UnrolledLinkedList()
        L.append(a).append(b)
        L[1] = c
        self.assertEqual(str(L[1]), '%d' % c)

    # PBT test
    @settings(max_examples=10)
    @given(a=st.integers(), b=st.integers(), c=st.integers())
    def test_iteration(self, a, b, c):
        L = UnrolledLinkedList()
        L.append(a).append(b).append(c)
        arr = []
        for i in L:
            arr.append(i)

        self.assertEqual(arr[0], L[0])
        self.assertEqual(arr[1], L[1])
        self.assertEqual(arr[2], L[2])

    # PBT test
    @settings(max_examples=10)
    @given(a=st.integers(), b=st.integers(), c=st.integers(), d=st.integers())
    def test_len(self, a, b, c, d):
        L = UnrolledLinkedList().append(a).append(b).append(c)
        L1 = UnrolledLinkedList().append(b).append(c).append(a)
        self.assertEqual(len(L), len(L1))

        L.append(d)

        self.assertEqual(str(len(L)), '4')

    # PBT test
    @settings(max_examples=10)
    @given(a=st.integers(), b=st.integers(), c=st.integers())
    def test_reverse(self, a, b, c):
        testL = [a, b, c]
        L = UnrolledLinkedList()
        L.append(c).append(b).append(a)

        newL = []

        for x in reversed(L):
            newL.append(x)
        self.assertEqual(newL, testL)

    # PBT test
    @settings(max_examples=10)
    @given(a=st.integers(), b=st.integers(), c=st.integers())
    def test_member(self, a, b, c):
        L = UnrolledLinkedList().append(a).append(b).append(c)

        self.assertEqual(a in L, True)
        self.assertEqual(c in L, True)

    # PBT test
    @settings(max_examples=10)
    @given(a=st.integers(), b=st.integers(), c=st.integers(), d=st.integers(),
           e=st.integers(), f=st.integers(), g=st.integers())
    def test_variable(self, a, b, c, d, e, f, g):
        L = UnrolledLinkedList()
        L.append(a).append(b).append(c).append(d).append(e).append(f).append(g)
        self.assertEqual(str(L), '{[%d, %d], [%d, %d], [%d, %d, %d]}'
                         % (a, b, c, d, e, f, g))

    # PBT test
    @settings(max_examples=10)
    @given(a=st.integers(), b=st.integers(), c=st.integers(), d=st.integers())
    def test_to_list(self, a, b, c, d):
        L = UnrolledLinkedList()
        L.append(a).append(b).append(c).append(d)
        self.assertEqual(str(L.to_list()), '[%d, %d, %d, %d]' % (a, b, c, d))

    # PBT test
    @settings(max_examples=10)
    @given(a=st.integers(), b=st.integers(), c=st.integers())
    def test_from_list(self, a, b, c):
        list1 = [a, b, c]
        L = UnrolledLinkedList()
        self.assertEqual(str(L.from_list(list1)), '{[%d, %d, %d]}' % (a, b, c))

    def test_filter(self):
        L = UnrolledLinkedList()
        L.append(1).append(2).append(3)
        self.assertEqual(str(L.filter(is_even)), '{[2]}')
        L1 = UnrolledLinkedList()
        L1.append(1).append(2).append(3)
        self.assertEqual(str(L1.filter(is_odd)), '{[1, 3]}')

    def test_findByValue(self):
        L = UnrolledLinkedList()
        L.append(1).append(2).append(3).append(1)
        self.assertEqual(str(L.findByValue(1)), '[0, 3]')

    # PBT test
    @settings(max_examples=10)
    @given(a=st.integers(), b=st.integers(), c=st.integers(), d=st.integers())
    def test_concat(self, a, b, c, d):
        ls = [a, b, c, d]
        ls.sort()
        a = ls[0]
        b = ls[1]
        c = ls[2]
        d = ls[3]
        L1 = UnrolledLinkedList().append(d).append(a)
        L2 = UnrolledLinkedList().append(b).append(c)
        # because the concat function will make them sorted
        self.assertEqual(str(L1.concat(L2)), '{[%d, %d, %d, %d]}'
                         % (a, b, c, d))
        self.assertEqual(str(L1.concat(L2)), str(L2.concat(L1)))

    def test_empty_function(self):
        L = UnrolledLinkedList().empty()
        self.assertEqual(str(L), '{}')

    # PBT test
    @settings(max_examples=10)
    @given(a=st.integers(), b=st.integers(), c=st.integers())
    def test_reduce(self, a, b, c):
        L = UnrolledLinkedList()
        self.assertEqual(L.reduce(_sum, 0), 0)

        L = UnrolledLinkedList()
        L = L.from_list([a, b, c])
        self.assertEqual(L.reduce(_sum, 0), a + b + c)
