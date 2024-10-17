class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"


def convert_list_to_list_node(input_values: list) -> ListNode:

    if not input_values:
        return None

    next_node = None

    for num in input_values[::-1]:
        current_node = ListNode(val=num, next=next_node)
        next_node = current_node

    return current_node


def convert_list_node_to_list(input_node: ListNode) -> list:

    output_list = []
    current_node = input_node
    while current_node:
        output_list.append(current_node.val)
        current_node = current_node.next

    return output_list


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        carry_over = 0

        try:
            l1_val = l1.val
        except AttributeError:
            l1_val = 0
        try:
            l2_val = l2.val
        except AttributeError:
            l2_val = 0

        add_value = l1_val + l2_val + carry_over

        if add_value > 9:
            add_value -= 10
            carry_over = 1
        else:
            carry_over = 0

        root_node = ListNode(val=add_value, next=None)
        last_node = root_node

        try:
            l1 = l1.next
        except AttributeError:
            l1 = None
        try:
            l2 = l2.next
        except AttributeError:
            l2 = None

        while l1 or l2 or carry_over:

            try:
                l1_val = l1.val
            except AttributeError:
                l1_val = 0
            try:
                l2_val = l2.val
            except AttributeError:
                l2_val = 0

            add_value = l1_val + l2_val + carry_over

            if add_value > 9:
                add_value -= 10
                carry_over = 1
            else:
                carry_over = 0
            current_node = ListNode(val=add_value, next=None)

            last_node.next = current_node
            last_node = current_node

            try:
                l1 = l1.next
            except AttributeError:
                l1 = None
            try:
                l2 = l2.next
            except AttributeError:
                l2 = None

        return root_node
