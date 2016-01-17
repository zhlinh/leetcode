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
        if len(digits) == 0:
            return []
        rList = [""]
        for i in range(len(digits)):
            dStr = dList[int(digits[i])]
            if dStr == "":
                continue
            tmpList = []
            for c in dStr:
                for r in rList:
                    tmpList.append(r + c)
            rList = tmpList
        return rList
