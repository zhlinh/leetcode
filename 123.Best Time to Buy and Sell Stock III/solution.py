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
        hold1, release1, hold2, release2 = -2 ** 31, 0, -2 ** 31, 0
        for price in prices:
        # The order could be changed,
        # because the following operations can be done in one day.
            release2 = max(release2, hold2 + price)
            hold2 = max(hold2, release1 - price)
            release1 = max(release1, hold1 + price)
            hold1 = max(hold1, -price)
        return release2
