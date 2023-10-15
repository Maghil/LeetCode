# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode("")
        current_node=ListNode("")
        initial=True
        while list1 or list2:
            if list2==None or (list1 and list1.val<= list2.val):
                node=ListNode(list1.val)
                list1=list1.next
            else:
                node=ListNode(list2.val)
                list2=list2.next
            if initial:
                head=node
                current_node=head
                initial=False
            else:
                current_node.next=node
                current_node=current_node.next
        return head    