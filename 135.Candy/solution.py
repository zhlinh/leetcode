#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-14
Last_modify:    2016-03-14
******************************************
'''

'''
There are N children standing in a line.
Each child is assigned a rating value.

You are giving candies to these children
subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
'''

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candies = [1 for _ in range(n)]
        num = n
        for i in range(1, n):
            if ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
                num += candies[i-1] + 1 - candies[i]
                candies[i] = candies[i-1] + 1
        for i in reversed(range(n - 1)):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                num += candies[i+1] + 1 - candies[i]
                candies[i] = candies[i+1] + 1
        return num
