from python_problems.src.utils.linked_list_utils import ListNode

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        """
        Merges two sorted linked lists given the head of each

        Since the lists are sorted, we can do this in one pass with a pointer for each list.
        Initialize two pointers, one for the head of each list.
        If the value of the first node is greater than the second node,

        :param list1: head node of first list
        :param list2: head node of second list
        :return: head node of combined list
        """

        # Return other list if either list is None

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val is None:
            return list2
        if list2.val is None:
            return list1

        pointer_1 = list1
        pointer_2 = list2

        if pointer_1.val > pointer_2.val:
            output_head = pointer_2
            pointer_2 = pointer_2.next
        else:
            output_head = pointer_1
            pointer_1 = pointer_1.next

        output_node = output_head
        # While both still have nodes to traverse
        # compare which list has the higher value node
        # Add that node as the next of the output list
        #
        while pointer_1 and pointer_2:
            if pointer_1.val > pointer_2.val:
                output_node.next = pointer_2
                pointer_2 = pointer_2.next
            else:
                output_node.next = pointer_1
                pointer_1 = pointer_1.next
            output_node = output_node.next

        if pointer_1:
            output_node.next = pointer_1


        if pointer_2:
            output_node.next = pointer_2

        return output_head
