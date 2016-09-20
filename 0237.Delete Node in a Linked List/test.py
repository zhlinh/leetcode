#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution
from solution import ListNode

def mkListNode(nums, p):
    """
    :type: nums: List
    :rtype: ListNode
    """
    head = lnp = ListNode(0)
    ret = None
    for i in range(len(nums)):
        lnp.next = ListNode(nums[i])
        lnp = lnp.next
        if lnp.val == p:
            ret = lnp
    return head.next, ret

def lsListNode(head):
    """
    :type: head: ListNode
    :rtype: List
    """
    lnp = head
    rList = []
    while lnp != None:
        rList.append(lnp.val)
        lnp = lnp.next
    return rList

inpt, p = mkListNode([1, 2, 3, 4, 5], 3)
sol = Solution()
res = sol.deleteNode(p)
print(lsListNode(inpt))
