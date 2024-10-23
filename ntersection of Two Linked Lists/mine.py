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
    def getIntersectionNode(self, head1, head2):
        current_node_1, current_node_2 = head1, head2
        list_1_count, list_2_count = 1, 1
        while current_node_1.next != None or current_node_2.next != None:
            if current_node_1.next != None:
                list_1_count += 1
                current_node_1 = current_node_1.next
            if current_node_2.next != None:
                list_2_count += 1
                current_node_2 = current_node_2.next
        if current_node_1 != current_node_2:
            return None
        else:
            while list_1_count != list_2_count:
                if list_1_count > list_2_count:
                    head1 = head1.next
                    list_1_count -= 1
                else:
                    head2 = head2.next
                    list_2_count -= 1
        while head1 != head2:
            head1 = head1.next
            head2 = head2.next
        return head1.value


if __name__ == "__main__":
    list_1 = MyLinkedList()
    list_1.addAtHead(-7)
    list_1.addAtHead(-6)
    list_1.addAtHead(-5)
    list_1.addAtHead(4)
    list_1.addAtHead(3)
    list_1.addAtHead(2)
    list_1.addAtHead(1)
    list_1.print()
    list_2 = MyLinkedList()
    list_2.addAtHead(-4)
    list_2.head.next = list_1.head.next.next.next.next
    list_2.addAtHead(-3)
    list_2.print()
    a = Solution()
    print(a.getIntersectionNode(list_1.head, list_2.head))
