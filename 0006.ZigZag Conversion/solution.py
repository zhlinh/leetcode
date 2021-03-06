#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-01-08
Last_modify:    2016-01-08
******************************************

'''

'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this: (you may want to display this pattern in a fixed font for better
legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number
of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

n=4:
P     I     N
A   L S   I G
Y A   H R
P     I

n=5:
P       H
A     S I
Y   I   R
P L     I G
A       N

'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        cons = ["" for row in range(numRows)]
        if numRows <= 1:
            return s
        nRow, step = 0, 1
        for c in s:
            cons[nRow] += c
            nRow += step
            if nRow == 0 or nRow == numRows-1:
                step = -step
        return ''.join(cons)
