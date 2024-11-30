class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def addAtHead(self, value):
        node = Node(value)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def print(self) -> None:
        current_node = self.head
        output = ""
        while current_node != None:
            output = output + str(current_node.value) + " "
            current_node = current_node.next
        print(output)

    def create(self, values) -> None:
        for value in values[::-1]:
            self.addAtHead(value)


class Solution:
    def isPalindrome(self, head):
        slow_pointer = fast_pointer = head
        while fast_pointer and fast_pointer.next and fast_pointer.next.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        print(fast_pointer.value)
        print(slow_pointer.value)

    def reverseList(self, list):
        previous_node = next_node = None
        current_node = list.head
        while current_node:
            next_node = current_node.next
            current_node.next=previous_node
            previous_node=current_node
            current_node=next_node
        return previous_node


if __name__ == "__main__":
    a = Solution()
    b = [1, 2, 3, 4, 5, 6, 7, 8]
    list1 = LinkedList()
    list1.create(b)
    list1.print()
    a.isPalindrome(list1.head)
