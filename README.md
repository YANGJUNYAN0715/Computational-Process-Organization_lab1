# GROUP: 123456 - lab 1 - variant 1

Author:

Junyan Yang(1310204834@qq.com)

Haodong Guo(guohaodong@hdu.edu.cn)

## Project structure

- `unrolled_linked_list.py` -- implementation of `UnrolledLinkedList`

class with `hello` and `add` features. Stateless.

- `unrolled_linked_list_test.py` -- unit and tests for

`UnrolledLinkedList`.

## Features

- test: `test_default_node_capacity`
- test: `test_custom_node_capacity`
- test: `test_empty`
- test: `test_delete_item`
- test: `test_get_item`
- test: `test_set_item`
- test: `test_iteration`
- test: `test_len`
- test: `test_member`
- test: `test_variable`
- test: `test_to_list`
- test: `test_from_list`
- test: `test_filter`
- test: `test_concat`

## Contribution

Junyan Yang(1310204834@qq.com) -- writes the main code of this lab

Donghao Guo(guohaodong@hdu.edu.cn) -- runs the tests.

## Changelog

- 14.04.2022 - 0
  - Initial
- 18.04.2022 - 1
  - Pass the workflow
- 24.04.2022 - 2
  - Modify the structure and update README.md
- 06.05.2022 - 3
  - Add some functions

## Design notes

An unrolled linked list is a linear data structure
that is a variant on the linked list.
Instead of just storing 1 element at each node,
unrolled linked lists store an entire array at each node.
