from unittest import TestCase

from python_problems.src.add_two_numbers import Solution, convert_list_to_list_node, ListNode, convert_list_node_to_list


class TestUtil(TestCase):

    def test_convert_list_to_node(self):
        test_num_list_1 = [2, 4, 3]

        root_node = convert_list_to_list_node(test_num_list_1)
        assert 2 == root_node.val
        assert 4 == root_node.next.val
        assert 3 == root_node.next.next.val
        assert root_node.next.next.next is None

    def test_convert_node_to_list(self):
        expected_output = [7, 0, 8]
        last_node = ListNode(val=8, next=None)
        middle_node = ListNode(val=0, next=last_node)
        root_node = ListNode(val=7, next=middle_node)
        actual_output = convert_list_node_to_list(root_node)
        assert expected_output == actual_output


class TestAdd2Numbers(TestCase):

    def test_simple_case(self):
        test_num_list_1 = [2, 3, 3]
        test_num_list_2 = [5, 6, 1]
        expected_output = [7, 9, 4]

        test_root_1 = convert_list_to_list_node(test_num_list_1)
        test_root_2 = convert_list_to_list_node(test_num_list_2)

        added_root = Solution().addTwoNumbers(test_root_1, test_root_2)
        converted_output = convert_list_node_to_list(added_root)

        assert expected_output == converted_output

    def test_simple_carry_case(self):
        test_num_list_1 = [2, 4, 3]
        test_num_list_2 = [5, 6, 4]
        test_root_node_1 = convert_list_to_list_node(test_num_list_1)
        test_root_node_2 = convert_list_to_list_node(test_num_list_2)

        added_num = Solution().addTwoNumbers(test_root_node_1, test_root_node_2)

        converted_output = convert_list_node_to_list(added_num)
        assert converted_output == [7, 0, 8]

    def test_dissimilar_lengths(self):
        test_num_list_1 = [9, 9, 9, 9, 9, 9, 9]
        test_num_list_2 = [9, 9, 9, 9]
        expected_output = [8, 9, 9, 9, 0, 0, 0, 1]

        test_root_1 = convert_list_to_list_node(test_num_list_1)
        test_root_2 = convert_list_to_list_node(test_num_list_2)

        added_root = Solution().addTwoNumbers(test_root_1, test_root_2)
        converted_output = convert_list_node_to_list(added_root)

        assert expected_output == converted_output

    def test_empty_list_2(self):
        test_num_list_1 = [9, 9]
        test_num_list_2 = []
        expected_output = [9, 9]

        test_root_1 = convert_list_to_list_node(test_num_list_1)
        test_root_2 = convert_list_to_list_node(test_num_list_2)

        added_root = Solution().addTwoNumbers(test_root_1, test_root_2)
        converted_output = convert_list_node_to_list(added_root)

        assert expected_output == converted_output

    def test_multiple_carry_case(self):
        test_num_list_1 = [2, 4, 3, 7, 4, 8]
        test_num_list_2 = [5, 6, 1, 7, 2, 6]
        expected_output = [7, 0, 5, 4, 7, 4, 1]

        test_root_1 = convert_list_to_list_node(test_num_list_1)
        test_root_2 = convert_list_to_list_node(test_num_list_2)

        added_root = Solution().addTwoNumbers(test_root_1, test_root_2)
        converted_output = convert_list_node_to_list(added_root)

        assert expected_output == converted_output

    def test_0th_case(self):
        test_num_list_1 = [0]
        test_num_list_2 = [0]
        test_root_node_1 = convert_list_to_list_node(test_num_list_1)
        test_root_node_2 = convert_list_to_list_node(test_num_list_2)

        added_num = Solution().addTwoNumbers(test_root_node_1, test_root_node_2)

        assert 0 == added_num.val
        assert added_num.next is None
