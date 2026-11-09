import unittest
from python_problems.src.merge_linked_lists import Solution
from python_problems.src.utils.linked_list_utils import (ListNode, create_linked_list, get_list_from_head)

class TestLinkedListMerge(unittest.TestCase):

    def test_simple_merge(self):
        input_first_list = [1, 4]
        input_second_list = [2, 3]
        expected_output = [1, 2, 3, 4]

        first_head = create_linked_list(input_first_list)
        second_head = create_linked_list(input_second_list)
        output_node = Solution().mergeTwoLists(first_head, second_head)
        output_list = get_list_from_head(output_node)
        assert output_list == expected_output

    def test_empty_merge(self):
        input_first_list = []
        input_second_list = []
        expected_output = []

        first_head = create_linked_list(input_first_list)
        second_head = create_linked_list(input_second_list)
        output_node = Solution().mergeTwoLists(first_head, second_head)
        output_list = get_list_from_head(output_node)
        assert output_list == expected_output

    def test_empty_first_list_merge(self):
        input_first_list = []
        input_second_list = [0,]
        expected_output = [0,]

        first_head = create_linked_list(input_first_list)
        second_head = create_linked_list(input_second_list)
        output_node = Solution().mergeTwoLists(first_head, second_head)
        output_list = get_list_from_head(output_node)
        assert output_list == expected_output

    def test_unitary_merge(self):
        input_first_list = [1,]
        input_second_list = [2,]
        expected_output = [1, 2]

        first_head = create_linked_list(input_first_list)
        second_head = create_linked_list(input_second_list)
        output_node = Solution().mergeTwoLists(first_head, second_head)
        output_list = get_list_from_head(output_node)
        assert output_list == expected_output

    def test_out_of_order_merge(self):
        input_first_list = [2,]
        input_second_list = [1,]
        expected_output = [1, 2]

        first_head = create_linked_list(input_first_list)
        second_head = create_linked_list(input_second_list)
        output_node = Solution().mergeTwoLists(first_head, second_head)
        output_list = get_list_from_head(output_node)
        assert output_list == expected_output

    def test_identical_merge(self):
        input_first_list = [2,]
        input_second_list = [2,]
        expected_output = [2, 2]

        first_head = create_linked_list(input_first_list)
        second_head = create_linked_list(input_second_list)
        output_node = Solution().mergeTwoLists(first_head, second_head)
        output_list = get_list_from_head(output_node)
        assert output_list == expected_output