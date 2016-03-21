#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-21
Last_modify:    2016-03-21
******************************************
'''

'''
Design a stack that supports
push, pop, top, and retrieving
the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dummy = LinkNode(0)
        self.min = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.dummy.next:
            new = LinkNode(0)
            self.min = x
        else:
            new = LinkNode(x-self.min)
            if x < self.min:
                self.min = x
        new.next = self.dummy.next
        self.dummy.next = new

    def pop(self):
        """
        :rtype: nothing
        """
        top = self.dummy.next
        if top:
            if top.val < 0:
                self.min = self.min - top.val
            self.dummy.next = top.next

    def top(self):
        """
        :rtype: int
        """
        top = self.dummy.next
        if top:
            if top.val > 0:
                return top.val + self.min
            else:
                return self.min
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
