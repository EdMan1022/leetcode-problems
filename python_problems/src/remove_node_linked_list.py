class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values: list) -> ListNode:

    next_node = None
    for value in values[::-1]:
        this_node = ListNode(val=value, next=next_node)
        next_node = this_node

    return this_node

def get_list_from_head(head: ListNode) -> list[int]:
    output_list = []
    current_node = head
    while current_node:
        output_list.append(current_node.val)
        current_node = current_node.next
    return output_list


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        """
        Removes the node from a linked list that is n spaces from the end of the list

        Does this by creating two pointers, one n spaces behind the other.
        When the first pointer hits the end of the list,
        the other pointer is pointing at the node to remove
        :param head:
        :param n:
        :return: head of the linked list, with the node removed
        """

        n -= 1

        pointer_1 = head
        pointer_2 = head  # This will point to the node to remove when pointer 1 hits the end of the list

        jumps = 0
        length = 0

        while pointer_1:
            length += 1
            if jumps < n + 2:
                pointer_1 = pointer_1.next
                jumps += 1
            else:
                pointer_1 = pointer_1.next
                pointer_2 = pointer_2.next

        if n + 1 == length:
            return head.next

        pointer_2.next = pointer_2.next.next
        return head
