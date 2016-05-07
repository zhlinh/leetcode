#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-07
Last_modify:    2016-05-07
******************************************
'''

'''
Convert a non-negative integer to its english words representation.
Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Hint:

Did you see a pattern in dividing the number into chunk of words?
For example, 123 and 123000.
Group the number by thousands (3 digits).
You can write a helper function that takes a number less than 1000
and convert just that chunk to words.
There are many edge cases. What are some good test cases?
Does your code work with input such as 0? Or 1000010?
(middle chunk is zero and should not be printed out)
'''

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        self.dic1 = ["Zero", "One", "Two", "Three", "Four", "Five", \
                    "Six", "Seven", "Eight", "Nigh", "Ten", \
                    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", \
                    "Sixteen", "Seventeen", "Eighteen", "Nighteen"]
        self.dic2 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", \
                     "Sixty", "Seventy", "Eighty", "Nighty"]
        self.dic3 = ["Thousand", "Million", "Thousand", "Billion"]
        res = ""
        last = num % 1000
        i = 0
        while num > 0:
            sub = self.helper(last)
            if sub and res:
                res = " " + res
            res = sub + res
            num //= 1000
            last = num % 1000
            if last > 0:
                res = self.dic3[i] + " " + res
            i = (i + 1) % 4
        return res

    def helper(self, num):
        res = ""
        if num // 100 > 0:
            res += self.dic1[num // 100] + " Hundred"
        num %= 100
        if num > 0:
            if res != "":
                res = res + " "
            if num // 10 > 1:
                res += self.dic2[num // 10] + " " + self.dic1[num % 10]
            else:
                res += self.dic1[num]
        return res or "Zero"

