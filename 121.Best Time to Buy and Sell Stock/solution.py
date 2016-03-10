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
Say you have an array for which the ith element
is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = 0
        maxProfit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if dp < 0:
                dp = diff
            else:
                dp += diff
            maxProfit = max(maxProfit, dp)
        return maxProfit
