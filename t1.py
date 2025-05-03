from typing import Optional


class Node:
    def __init__(self, data: Optional[int] = None):
        self.data: Optional[int] = data
        self.next: Optional["Node"] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def insert_at_end(self, data: int) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current: Node = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse(self) -> None:
        prev: Optional[Node] = None
        current: Optional[Node] = self.head
        while current:
            next_node: Optional[Node] = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self) -> None:
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        return self._merge(left, right)

    def _merge(self, left: Optional[Node], right: Optional[Node]) -> Optional[Node]:
        if not left:
            return right
        if not right:
            return left

        if left.data <= right.data:
            result = left
            result.next = self._merge(left.next, right)
        else:
            result = right
            result.next = self._merge(left, right.next)

        return result

    def _get_middle(self, head: Node) -> Node:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def merge_two_sorted(list1: "LinkedList", list2: "LinkedList") -> "LinkedList":
        merged_list = LinkedList()
        dummy = Node(0)
        current = dummy

        l1 = list1.head
        l2 = list2.head

        while l1 and l2:
            if l1.data <= l2.data:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 if l1 else l2
        merged_list.head = dummy.next
        return merged_list


# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    for value in [50, 10, 30, 20, 40]:
        ll.insert_at_end(value)

    print("Original list:")
    ll.print_list()

    ll.reverse()
    print("Reversed list:")
    ll.print_list()

    ll.sort()
    print("Sorted list:")
    ll.print_list()

    ll2 = LinkedList()
    for value in [4, 2, 6]:
        ll2.insert_at_end(value)
    ll2.sort()

    print("List 2:")
    ll2.print_list()

    merged = LinkedList.merge_two_sorted(ll, ll2)
    print("Merged Sorted List:")
    merged.print_list()
