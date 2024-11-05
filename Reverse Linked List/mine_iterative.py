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
    def reverseList(self, head):
        cur_node = head
        prev_node = next_node = None
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        return prev_node


if __name__ == "__main__":
    list = LinkedList()
    a = Solution()
    list.create_list([])
    list.print()
    list.head = a.reverseList(list.head)
    list.print()
