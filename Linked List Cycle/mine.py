class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class MyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def print(self) -> None:
        current_node = self.head
        output = ""
        while current_node != None:
            output = output + str(current_node.value) + " "
            current_node = current_node.next
        print(output)


class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False


if __name__ == "__main__":
    my_list = MyLinkedList()
    my_list.addAtHead(-4)
    my_list.addAtHead(0)
    my_list.addAtHead(2)
    my_list.addAtHead(3)
    my_list.print()
    a = Solution()
    print(a.hasCycle(my_list.head))
