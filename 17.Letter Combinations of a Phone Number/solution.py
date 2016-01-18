#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-01-16
Last_modify:    2016-01-16
******************************************
'''

'''
Given a digit string, return all possible letter combinations that the number
could represent.

A mapping of digit to letters is just like on the telephone buttons.

    Input:Digit string "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in
any order you want.
'''

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dList = ["", "", "abc", "def", "ghi", "jkl", \
                 "mno", "pqrs", "tuv", "wxyz"]
        rList = []
        if len(digits) == 0:
            return []
        self.dfs(digits, dList, 0, "", rList)
        return rList

    def dfs(self, digits, dic, depth, path, res):
        if depth == len(digits):
            res.append(path)
            return None
        # incase for digits[i] == 0 or 1
        if dic[int(digits[depth])] == "":
            depth += 1
        for c in dic[int(digits[depth])]:
            self.dfs(digits, dic, depth + 1, path + c, res)
