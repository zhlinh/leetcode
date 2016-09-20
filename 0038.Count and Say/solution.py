#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-17
Last_modify:    2016-02-17
******************************************
'''

'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        curr = "1"
        for i in range(n - 1):
            count = 1
            prev = curr
            say = prev[0]
            curr = ""
            for j in range(1, len(prev)):
                if prev[j] == say:
                    count += 1
                else:
                    curr += str(count) + say 
                    count = 1
                    say = prev[j]
            curr += str(count) + say
        return curr
