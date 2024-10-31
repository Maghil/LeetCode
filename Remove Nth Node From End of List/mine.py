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

    def create_list(self, values) -> None:
        for value in values[::-1]:
            self.addAtHead(value)


class Solution:
    def removeNthFromEnd(self, head, n):
        first_node = second_node = head
        while first_node and first_node.next != None:
            if n <= 0:
                second_node = second_node.next
            n -= 1
            first_node = first_node.next
        if n == 1:
            return head.next
        else:
            second_node.next = second_node.next.next
        return head


if __name__ == "__main__":
    list = LinkedList()
    a = Solution()
    list.create_list([1,2,3,4,5])
    list.print()
    print(a.removeNthFromEnd(list.head, 2).next.next.next.value)
