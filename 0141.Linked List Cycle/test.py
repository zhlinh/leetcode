#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution
from solution import ListNode

def mkListNode(nums, i, dic):
    """
    :type: nums: List
    :rtype: ListNode
    """
    if nums[i] in dic:
        return dic[nums[i]]
    head = ListNode(nums[i])
    dic[nums[i]] = head
    if i + 1 < len(nums):
        head.next = mkListNode(nums, i + 1, dic)
    return head

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

dic = {}
inpt = mkListNode([3, 2, 0, -4, 2], 0, dic)
sol = Solution()
res = sol.hasCycle(inpt)
print(res)
