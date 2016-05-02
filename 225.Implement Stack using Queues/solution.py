#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-01
Last_modify:    2016-05-01
******************************************
'''

'''
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means
only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively.
You may simulate a queue by using a list or deque (double-ended queue),
as long as you use only standard operations of a queue.
You may assume that all operations are valid
(for example, no pop or top operations will be called on an empty stack).
Update (2015-06-11):
The class name of the Java function had been updated to MyStack instead of Stack.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and all test cases.
'''

from collections import deque

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """

        self.q = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        """
        :rtype: nothing
        """
        return self.q.popleft()

    def top(self):
        """
        :rtype: int
        """
        if self.q:
            return self.q[0]
        else:
            return None

    def empty(self):
        """
        :rtype: bool
        """
        return False if self.q else True
