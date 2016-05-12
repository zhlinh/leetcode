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
        n = len(s)
        rmLNum, rmRNum = 0, 0
        results = set()
        for c in s:
            if c == '(':
                rmLNum += 1
            if c == ')':
                if rmLNum > 0:
                    rmLNum -= 1
                else:
                    rmRNum += 1
        self.dfs(s, 0, n, rmLNum, rmRNum, 0, "", results)
        return list(results)


    def dfs(self, s, pos, n, rmLNum, rmRNum, stack, result, results):
        if pos == n and (rmLNum | rmRNum | stack) == 0:
            results.add(''.join(result))
            return
        if pos == n or rmLNum < 0 or rmRNum < 0 or stack < 0:
            return
        if s[pos] == '(':
            self.dfs(s, pos + 1, n, rmLNum - 1, rmRNum, stack, result, results)
            self.dfs(s, pos + 1, n, rmLNum, rmRNum, stack + 1, result + s[pos], results)
        elif s[pos] == ')':
            self.dfs(s, pos + 1, n, rmLNum, rmRNum - 1, stack, result, results)
            self.dfs(s, pos + 1, n, rmLNum, rmRNum, stack - 1, result + s[pos], results)
        else:
            self.dfs(s, pos + 1, n, rmLNum, rmRNum, stack, result + s[pos], results)
