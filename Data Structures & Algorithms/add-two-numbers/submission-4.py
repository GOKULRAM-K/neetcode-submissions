# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            current = dummy

            carry = 0

            while l1 and l2:
                val = (l1.val + l2.val + carry)%10
                node = ListNode(val, None)
                current.next = node
                current = node
                carry = (l1.val + l2.val + carry)//10

                l1 = l1.next
                l2 = l2.next

            while l1:
                node = ListNode((l1.val + carry)%10, None)
                current.next = node
                current = node
                carry = (l1.val + carry)//10

                l1 = l1.next
                            
            while l2:
                node = ListNode((l2.val + carry)%10, None)
                current.next = node
                current = node
                carry = (l2.val + carry)//10
                
                l2 = l2.next
                
            if carry:
                node = ListNode(carry, None)
                current.next = node    
            return dummy.next
