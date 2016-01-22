#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-01-21
Last_modify:    2016-01-21
******************************************
'''

'''
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rList = []
        self.dfs(n, n, "", rList)
        return rList

    def dfs(self, left, right, path, res):
        if left > right:
            return
        if not right:
            res.append(path)
            return
        if left:
            self.dfs(left - 1, right, path + "(", res)
        if right:
            self.dfs(left, right - 1, path + ")", res)
