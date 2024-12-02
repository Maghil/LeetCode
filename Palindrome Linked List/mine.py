class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, vals=None) -> None:
        self.head = None
        if vals:
            self.create(vals)

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
        while current_node != None:
            output = output + str(current_node.val) + " "
            current_node = current_node.next
        print(output)

    def create(self, vals) -> None:
        for val in vals[::-1]:
            self.addAtHead(val)


class Solution:
    def isPalindrome(self, head):
        slow_pointer = fast_pointer = head
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        slow_pointer = self.reverseList(slow_pointer)
        fast_pointer = head
        while slow_pointer:
            if slow_pointer.val != fast_pointer.val:
                return False
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        return True

    def reverseList(self, head):
        previous_node = None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node, current_node = current_node, next_node
        return previous_node


if __name__ == "__main__":
    a = Solution()
    b = [1, 2, 3, 4, 4, 3, 2, 1]
    c = [1, 2, 3, 2, 1]
    d = [1, 2, 3, 3, 5, 1]
    e = [1]
    list1 = LinkedList(b)
    list2 = LinkedList(c)
    list3 = LinkedList(d)
    list4 = LinkedList(e)
    list1.print()
    print(a.isPalindrome(list1.head))
    list2.print()
    print(a.isPalindrome(list2.head))
    list3.print()
    print(a.isPalindrome(list3.head))
    list4.print()
    print(a.isPalindrome(list4.head))

# 1 2 3 4 4 3 2 1 ; 1 1
# 1 2 3 4 4 3 2 1 ; 2 3
# 1 2 3 4 4 3 2 1 ; 3 4
# 1 2 3 4 4 3 2 1 ; 4 2

# 1 2 3 2 1 ; 1 1
# 1 2 3 2 1 ; 2 3
# 1 2 3 2 1 ; 3 1
