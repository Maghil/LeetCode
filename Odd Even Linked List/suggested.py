class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def addAtHead(self, val):
        node = Node(val)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def print(self) -> None:
        current_node = self.head
        output = ""
        while current_node:
            output = output + str(current_node.val) + " "
            current_node = current_node.next
        print(output)

    def create_list(self, vals) -> None:
        for val in vals[::-1]:
            self.addAtHead(val)


class Solution(object):
    def oddEvenList(self, head):
        if head == None or head.next == None:
            return head
        odd = Node(0)
        odd_ptr = odd
        even = Node(0)
        even_ptr = even
        idx = 1
        while head != None:
            if idx % 2 == 0:
                even_ptr.next = head
                even_ptr = even_ptr.next
            else:
                odd_ptr.next = head
                odd_ptr = odd_ptr.next
            head = head.next
            idx += 1
        even_ptr.next = None
        odd_ptr.next = even.next
        return odd.next


if __name__ == "__main__":
    list = LinkedList()
    a = Solution()
    list.create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    list.print()
    list.head = a.oddEvenList(list.head)
    list.print()
