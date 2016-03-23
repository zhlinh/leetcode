#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-10
Last_modify:    2016-03-10
******************************************
'''

'''
Say you have an array for which the ith element is the price of
a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the
same time (ie, you must sell the stock before you buy again).
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        k = 2
        hold = [-2 ** 31] * (k + 1)
        release = [0] * (k + 1)
        for p in prices:
            for i in range(1, k + 1):
                hold[i] = max(hold[i], release[i-1] - p)
                release[i] = max(release[i], hold[i] + p)
        return release[k]
