# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:
            return list2
        elif list2==None:
            return list1
        else:
            if list1.val<list2.val:
                return(self.merger(list1,list2))
            else:
                return(self.merger(list2,list1))

    def merger(self,list1,list2):
        head = list1
        done=False
        while list2!=None and not done:
            if list1.next==None:
                list1.next=list2
                done=True
            elif list2.val <= list1.next.val:
                node=list2
                list2=list2.next
                node.next=list1.next
                list1.next=node
                list1=list1.next
            else:
                list1=list1.next
        return head

        