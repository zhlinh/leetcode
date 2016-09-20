#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-09
Last_modify:    2016-05-09
******************************************
'''

'''
Given a string that contains only digits 0-9 and a target value,
return all possibilities to add binary operators (not unary)
+, -, or * between the digits so they evaluate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
Credits:
Special thanks to @davidtan1890 for adding this problem
and creating all test cases.
'''

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        results = []
        if num:
            self.dfs(num, target, 0, 0, 0, "", results)
        return results

    def dfs(self, num, target, pos, val, backup, result, results):
        if pos >= len(num):
            if val == target:
                results.append(result)
            return
        for i in range(pos, len(num)):
            if i != pos and num[pos] == "0":
                break
            cur = int(num[pos:i+1])
            if pos == 0:
                self.dfs(num, target, i + 1, cur, cur, \
                        result + str(cur), results)
            else:
                self.dfs(num, target, i + 1, val + cur, cur, \
                        result + "+" + str(cur), results)
                self.dfs(num, target, i + 1, val - cur, -cur, \
                        result + "-" + str(cur), results)
                self.dfs(num, target, i + 1, val - backup + backup * cur, \
                        backup * cur, result + "*" + str(cur), results)
