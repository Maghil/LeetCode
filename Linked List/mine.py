class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index > self.length-1 or index < 0:
            return -1
        else:
            current_node = self.head
            for _ in range(0, index):
                current_node = current_node.next
        return current_node.value

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length or index < 0:
            return -1
        elif index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            new_node = Node(val)
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            print(current_node.value)
            new_node.prev = current_node.prev
            new_node.next = current_node
            current_node.prev.next = new_node
            current_node.prev = new_node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        if index == 0:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            currNode = self.head
            for _ in range(index):
                currNode = currNode.next
            currNode.prev.next = currNode.next
            if currNode.next:
                currNode.next.prev = currNode.prev
        self.length -= 1

    def print(self) -> None:
        current_node = self.head
        output = ""
        while current_node != None:
            output = output + str(current_node.value) + " "
            current_node = current_node.next
        print(output)

    def printReverse(self) -> None:
        temp_tail = self.tail
        output = ""
        while temp_tail != None:
            output = output + str(temp_tail.value) + " "
            temp_tail = temp_tail.prev
        print(output)


# Your MyLinkedList object will be instantiated and called as such:
obj=MyLinkedList()
obj.addAtHead(7)
obj.addAtHead(2)
obj.addAtHead(1)
obj.addAtIndex(3,0)
obj.print()
obj.deleteAtIndex(2)
obj.print()
obj.addAtHead(6)
obj.print()
obj.addAtTail(4)
obj.print()
obj.get(4)
obj.addAtHead(4)
obj.addAtIndex(5,0)
obj.addAtHead(6)