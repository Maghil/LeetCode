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


class Solution:
    def oddEvenList(self, head):
        current_node = odd_head = head
        prev_node = odd_head = next_node = even_head = None
        counter = 1
        while current_node:
            next_node = current_node.next
            if counter == 1:
                odd_head = current_node
            elif counter == 2:
                even_head = current_node
            elif counter % 2 != 0:
                prev_node.next = current_node.next
                current_node.next = even_head
                odd_head.next = current_node
                odd_head = current_node
                current_node = current_node.next
            prev_node, current_node = current_node, next_node
            counter += 1
            print(counter, prev_node.val, odd_head.val)
        return head


if __name__ == "__main__":
    list = LinkedList()
    a = Solution()
    list.create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    list.print()
    list.head = a.oddEvenList(list.head)
    list.print()
