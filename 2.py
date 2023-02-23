# Definition for singly-linked list.
import itertools
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {str(self.next) if self.next else '[]'}"

    def __eq__(self, other):
        if other is None or self.val != other.val:
            return False
        else:
            return self.next == other.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry, rest = 0, None
        sol, head = None, None
        e1, e2 = l1, l2
        while True:
            carry, s = divmod(e1.val + e2.val + carry, 10)
            e = ListNode(val=s)
            if sol is not None:
                sol.next = e
            else:
                head = e
            sol = e

            e1, e2 = e1.next, e2.next
            if e1 is None:
                rest = e2
                break
            elif e2 is None:
                rest = e1
                break

        while rest:
            carry, s = divmod(rest.val + carry, 10)
            sol.next = ListNode(val=s)
            rest, sol = rest.next, sol.next

        if carry:
            sol.next = ListNode(val=carry)

        return head


if __name__ == '__main__':
    s = Solution()

    def to_ListNode(l: list):
        r = None
        for e in reversed(l):
            r = ListNode(val=e, next=r)
        return r

    assert s.addTwoNumbers(to_ListNode([2,4,3]), to_ListNode([5,6,4])) == to_ListNode([7,0,8])
    assert s.addTwoNumbers(to_ListNode([9,9,9,9,9,9,9]), to_ListNode([9,9,9,9])) == to_ListNode([8,9,9,9,0,0,0,1])
