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

- PBT test: `test_default_node_capacity`
- PBT test: `test_custom_node_capacity`
- PBT test: `test_empty`
- PBT test: `test_delete_item`
- PBT test: `test_get_item`
- PBT test: `test_set_item`
- PBT test: `test_iteration`
- PBT test: `test_len`
- PBT test: `test_member`
- PBT test: `test_variable`
- PBT test: `test_to_list`
- PBT test: `test_from_list`
- test: `test_filter`
- test: `test_findByValue`
- PBT test: `test_concat`
- test: `test_empty_function`
- PBT test: `test_reduce`

## Contribution

Junyan Yang(1310204834@qq.com) -- writes the main code of this lab

Donghao Guo(guohaodong@hdu.edu.cn) -- runs the tests and writes
some functions

## Changelog

- 14.04.2022 - 0
  - Initial
- 18.04.2022 - 1
  - Pass the workflow
- 24.04.2022 - 2
  - Modify the structure
  - Update README.md
- 06.05.2022 - 3
  - Add functions of concat and filter
  - Use PBT tests and hypothesis tests
- 08.05.2022 - 4
  - Add functions of empty and reduce
  - Use PBT tests
- 09.05.2022 - 5
  - Repair a mistake in function of concat
- 14.05.2022 - 6
  - Change function of filter into mutable
  - Add function of findByValue
  - Add docstrings for all functions and type hints

## Design notes

An unrolled linked list is a linear data structure
that is a variant on the linked list.
Instead of just storing 1 element at each node,
unrolled linked lists store an entire array at each node.
