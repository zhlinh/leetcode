#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-02
Last_modify:    2016-05-02
******************************************
'''

'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers,
+, -, *, / operators and empty spaces .
The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        res = 0
        sign = '+'
        stack = []
        n = len(s)
        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if (not s[i].isdigit() and s[i] != ' ') or i == n - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    tmp = stack.pop()
                    if tmp >= 0:
                        stack.append(tmp // num)
                    else:
                        stack.append(-(abs(tmp) // num))
                sign = s[i]
                num = 0
        for number in stack:
            res += number
        return res
