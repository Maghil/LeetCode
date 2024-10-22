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
        count = 0
        while current_node != None and count < 15:
            output = output + str(current_node.value) + " "
            current_node = current_node.next
            count += 1
        print(output)


class Solution:
    def detectCycle(self, head):
        slow = fast = head
        print(slow.value, fast.value)
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            print(slow.value, fast.value)
            if slow == fast:
                print("circle detected")
                print(slow.value, head.value)
                while head != slow:
                    head, slow = head.next, slow.next
                    print(slow.value, head.value)
                return head.value
        return None


if __name__ == "__main__":
    my_list = MyLinkedList()
    my_list.addAtHead(6)
    my_list.addAtHead(5)
    my_list.addAtHead(-4)
    my_list.addAtHead(0)
    my_list.addAtHead(2)
    my_list.addAtHead(3)
    head = my_list.head
    head.next.next.next.next.next.next = head.next.next.next.next.next
    my_list.print()
    a = Solution()
    print(a.detectCycle(my_list.head))
