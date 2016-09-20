#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-03
Last_modify:    2016-03-03
******************************************
'''

'''
Given a string containing only digits,
restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        result, results = [], []
        self.dfs(s, 0, n, result, results, 0)
        return(results)

    def dfs(self, s, start, n, result, results, depth):
        if start > n:
            return
        if depth >= 4:
            if start == n:
                results.append('.'.join(result))
            return
        for i in range(1, 4):
            if start < n and s[start] == '0':
                self.dfs(s, start + 1, n, result + [s[start:start+1]], results, depth + 1)
                break
            if i < 3 or (i == 3 and start < n and int(s[start:start+i]) <= 255):
                self.dfs(s, start + i, n, result + [s[start:start+i]], results, depth + 1)
