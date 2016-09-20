#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution
from solution import ListNode

def mkListNode(nums):
    """
    :type: nums: List
    :rtype: ListNode
    """
    head = lnp = ListNode(0)
    for i in range(len(nums)):
        lnp.next = ListNode(nums[i])
        lnp = lnp.next
    return head.next

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

inpt1 = mkListNode([2])
inpt2 = mkListNode([1])
sol = Solution()
res = sol.mergeTwoLists(inpt1, inpt2)
print(lsListNode(res))
