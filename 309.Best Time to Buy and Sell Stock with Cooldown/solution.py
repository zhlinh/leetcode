#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-15
Last_modify:    2016-05-15
******************************************
'''

'''
Say you have an array for which the i-th element is the price of a given
stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times)
with the following restrictions:

You may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day.
(ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        # s0:rest, s1:hold, s2:sold
        s0 = 0
        s1 = -prices[0]
        s2 = -2 ** 31
        for i in range(n):
            preS2 = s2
            s2 = s1 + prices[i]
            s1 = max(s1, s0 - prices[i])
            s0 = max(s0, preS2)
        return max(s0, s2)
