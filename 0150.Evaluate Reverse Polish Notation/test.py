#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

#  tokens =  ["4", "13", "5", "/", "+"]
#  tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens = ["4","-2","/","2","-3","-","-"]
sol = Solution()
res = sol.evalRPN(tokens)
print(res)
