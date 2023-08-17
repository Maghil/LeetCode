# NOTES
  1. dont use shortand operation in python as it take lot of space(it works by copying not like other languages) 16.30mb vs 16.44mb was huge
  2. Linked list solution needs a class for node and a class linked list containing operation
  3. we can work with node itself if we don't have any higher operation like print and insert in linked list
  4. linked list in python work as objects are storead as refence instead of value. so when we store next, the address of the node is stored
  5. Linked list struct

### LINKED LIST
```
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next 
```
```
class LinkedList:
  def __init__(self,head):
    self.head=head

  def insert(self,..):
    pass
```
