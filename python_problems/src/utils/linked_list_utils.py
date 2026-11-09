class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def create_linked_list(values: list) -> ListNode:

    if len(values) == 0:
        return ListNode(val=None, next=None)

    next_node = None
    for value in values[::-1]:
        this_node = ListNode(val=value, next=next_node)
        next_node = this_node

    return this_node

def get_list_from_head(head: ListNode) -> list[int]:
    output_list = []
    current_node = head
    if current_node and current_node.val is None:
        current_node = current_node.next
    while current_node:
        output_list.append(current_node.val)
        current_node = current_node.next
    return output_list

