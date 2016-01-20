#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-01-20
Last_modify:    2016-01-20
******************************************
'''

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lb = []
        rb = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in rb.values:
                lb.append(c)
            if c in rb.keys:
                if len(lb) == 0 or lb[-1] != rb[c]:
                    return False
                else:
                    lb.pop()
        return len(lb) == 0
