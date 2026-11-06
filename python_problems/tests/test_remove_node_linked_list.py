import unittest
from python_problems.src.remove_node_linked_list import Solution, ListNode, create_linked_list, get_list_from_head

class MyTestCase(unittest.TestCase):


    def test_create_linked_list(self):
        values = [1,2,3]
        first_node = create_linked_list(values)

        assert first_node.val == 1
        assert first_node.next.val == 2
        assert first_node.next.next.val == 3
        assert first_node.next.next.next is None

    def test_create_list_from_linked_list(self):
        values = [1, 2, 3]
        first_node = create_linked_list(values)

        output_list = get_list_from_head(first_node)
        assert output_list == [1, 2, 3]

    def test_node_removed(self):
        input_list = [1, 2, 3]
        test_n = 1
        expected_output = [1, 2]

        head = create_linked_list(input_list)
        output_node = Solution().removeNthFromEnd(head=head, n=test_n)
        output_list = get_list_from_head(output_node)
        assert output_list == expected_output


    def test_node_removed_2(self):
        input_list = [1, 2, 3]
        test_n = 2
        expected_output = [1, 3]

        head = create_linked_list(input_list)
        output_node = Solution().removeNthFromEnd(head=head, n=test_n)
        output_list = get_list_from_head(output_node)
        assert output_list == expected_output

    def test_node_removed_3(self):
        input_list = [1, 2, 3]
        test_n = 3
        expected_output = [2, 3]

        head = create_linked_list(input_list)
        output_node = Solution().removeNthFromEnd(head=head, n=test_n)
        output_list = get_list_from_head(output_node)
        assert output_list == expected_output

    def test_single_node_removed(self):
        input_list = [1]
        test_n = 1
        expected_output = []

        head = create_linked_list(input_list)
        output_node = Solution().removeNthFromEnd(head=head, n=test_n)
        output_list = get_list_from_head(output_node)
        assert output_list == expected_output

    def test_duo_node_removed(self):
        input_list = [1, 2]
        test_n = 1
        expected_output = [1]

        head = create_linked_list(input_list)
        output_node = Solution().removeNthFromEnd(head=head, n=test_n)
        output_list = get_list_from_head(output_node)
        assert output_list == expected_output

    def test_node_removed_longer(self):
        input_list = [1, 2, 3, 4, 5]
        test_n = 2
        expected_output = [1, 2, 3, 5]

        head = create_linked_list(input_list)
        output_node = Solution().removeNthFromEnd(head=head, n=test_n)
        output_list = get_list_from_head(output_node)
        assert output_list == expected_output

    def test_node_removed_longer_2(self):
        input_list = [1, 2, 3, 4, 5]
        test_n = 2
        expected_output = [1, 2, 3, 5]

        head = create_linked_list(input_list)
        output_node = Solution().removeNthFromEnd(head=head, n=test_n)
        output_list = get_list_from_head(output_node)
        assert output_list == expected_output

    def test_first_node_unmodified(self):

        head = create_linked_list([1, 2, 3])

        Solution().removeNthFromEnd(head=head, n=1)

        assert head.val == 1
