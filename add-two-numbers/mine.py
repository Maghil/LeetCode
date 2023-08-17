# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next            

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        prev_node=ListNode()
        while l1 != None or l2 != None:
            digit=0
            if l1!= None:
                digit+=l1.val
                l1=l1.next
            if l2!=None:
                digit+=l2.val
                l2=l2.next
            digit+=carry
            carry=0
            if digit > 9:
                carry=digit//10
                digit=digit%10
            current=ListNode(digit)
            if prev_node.val==None:
                head=ListNode()
                head=current
                prev_node=current
            else:
                prev_node.next=current
                prev_node=current
        if carry:
            current=ListNode(carry)
            prev_node.next=current
            prev_node=current
        return head
            
