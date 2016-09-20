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
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ),
the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.
'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        sign = 1
        res = 0
        stack = []
        for c in s:
            if c >= '0' and c <= '9':
                num = num * 10 + int(c)
            elif c == '+':
                res += sign * num
                num = 0
                sign = 1
            elif c == '-':
                res += sign * num
                num = 0
                sign = -1
            elif c == '(':
               stack.append(res)
               stack.append(sign)
               num = 0
               res = 0
               sign = 1
            elif c == ')':
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res
