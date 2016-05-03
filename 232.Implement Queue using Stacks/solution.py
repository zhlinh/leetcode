#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-03
Last_modify:    2016-05-03
******************************************
'''

'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack --
which means only push to top, peek/pop from top, size,
and is empty operations are valid.
Depending on your language, stack may not be supported natively.
You may simulate a stack by using a list or deque (double-ended queue),
as long as you use only standard operations of a stack.
You may assume that all operations are valid
(for example, no pop or peek operations will be called on an empty queue).
'''

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.in_stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.peek()
        self.out_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if self.in_stack or self.out_stack:
            return False
        return True
