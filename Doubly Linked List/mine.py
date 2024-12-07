class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self, values=None) -> None:
        self.head = None
        self.length = 0
        self.tail = None
        if values:
            self.create(values)

    def addAtHead(self, val):
        new = Node(val)
        if self.length != 0:
            self.head.prev = new
            new.next = self.head
            self.head = new
        else:
            self.head = self.tail = new
        self.length += 1

    def addAtTail(self, val):
        new = Node(val)
        if self.length != 0:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        else:
            self.tail = self.head = new
        self.length += 1

    def get(self, index):
        if index > self.length - 1 or index < 0:
            return -1
        print(f"{index=}")
        print(f"{self.length=}")
        current = self.head
        for _ in range(0, index):
            current = current.next
        return current.val

    def addAtIndex(self, index, val):
        if index > self.length - 1 or index < 0:
            return -1

        current = self.head
        for _ in range(0, index-1):
            current = current.next

        if index == 0:
            self.addAtHead(val)

        elif index == self.length:
            self.addAtTail(val)

        else:
            new = Node(val)
            next = current.next
            current.next = new
            new.prev = current
            new.next = next
            next.prev = new
            self.length += 1

    def deleteAtIndex(self, index):
        if index > self.length - 1 or index < 0:
            return -1

        current = self.head
        for _ in range(0, index):
            current = current.next

        if self.length == 1:
            self.head = None
            self.tail = None

        elif current == self.head:
            self.head = current.next
            self.head.prev = None

        elif current == self.tail:
            self.tail = current.prev
            self.tail.next = None

        else:
            current.prev.next, current.next.prev = current.next, current.prev

        self.length -= 1
        return self.head

    def create(self, values):
        for val in values[::-1]:
            self.addAtHead(val)

    def print(self):
        output = ""
        current = self.head
        while current:
            output = output + str(current.val) + " "
            current = current.next
        print(output)


# "deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
# ,[2],[6],[4],[4],[4],[5,0],[6]]

if __name__ == "__main__":
    a = MyLinkedList()
    a.addAtHead(7)
    a.print()
    a.addAtHead(2)
    a.print()
    a.addAtHead(1)
    a.print()
    a.addAtIndex(3,0)
    a.print()
    a.deleteAtIndex(2)
    a.print()
    a.addAtHead(6)
    a.print()
    a.addAtTail(4)
    a.print()
    a.get(4)
    a.print()
    a.addAtHead(4)
    a.print()
    a.addAtIndex(5,0)
    a.print()
    a.addAtHead(6)
    a.print()