#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-11
Last_modify:    2016-05-11
******************************************
'''

'''
Remove the minimum number of invalid parentheses in order to
make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
Credits:
Special thanks to @hpplayer for adding this problem and creating all test cases.
'''

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []
        self.dfs(s, ['(', ')'], 0, 0, results)
        return results


    def dfs(self, s, pair, start_i, start_j, results):
        stack = 0
        for i in range(start_i, len(s)):
            if s[i] == pair[0]:
                stack += 1
            if s[i] == pair[1]:
                stack -= 1
            # if valid, go forward
            if stack >= 0:
                continue
            for j in range(start_j, i + 1):
                if s[j] == pair[1] and (j == start_j or s[j] != s[j-1]):
                    self.dfs(s[:j] + s[j+1:], pair, i, j, results)
            return
        s = s[::-1]
        if pair[0] == '(':
            self.dfs(s, [')', '('], 0, 0, results)
        else:
            results.append(s)

