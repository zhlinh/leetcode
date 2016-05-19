#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-18
Last_modify:    2016-05-18
******************************************
'''

'''
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up
that amount. If that amount of money cannot be made up by any combination of
the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and
creating all test cases.
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 1:
            return 0
        coins.sort(reverse=True)
        self.times = 2 ** 31 - 1
        self.helper(coins, 0, 0, amount)
        return -1 if self.times == 2 ** 31 - 1 else self.times

    def helper(self, coins, pos, count, amount):
        if pos >= len(coins) or count + 2 > self.times:
            return
        maxN = amount // coins[pos]
        while maxN >= 0:
            newCount = count + maxN
            rem = amount - maxN * coins[pos]
            if rem > 0 and newCount + 1 < self.times:
                self.helper(coins, pos + 1, newCount, rem)
            else:
                if rem == 0 and newCount < self.times:
                    self.times = newCount
                break
            maxN -= 1
