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
    def removeElements(self, head, val):
        if val == 0:
            return head
        cur_node = head
        prev_node = next_node = None
        while cur_node:
            next_node = cur_node.next
            if cur_node.val == val:
                if prev_node:
                    prev_node.next = next_node
                else:
                    head = next_node
            else:
                prev_node = cur_node
            cur_node = next_node
        return head


if __name__ == "__main__":
    list = LinkedList()
    a = Solution()
    list.create_list([2, 2, 2, 2])
    list.print()
    list.head = a.removeElements(list.head, 2)
    list.print()
