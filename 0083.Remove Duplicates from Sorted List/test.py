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

inpt = mkListNode([1, 2, 3, 3, 4, 4, 5])
#  inpt = mkListNode([1, 1, 1])
sol = Solution()
res = sol.deleteDuplicates(inpt)
print(lsListNode(res))
