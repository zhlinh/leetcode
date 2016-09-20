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
There are N gas stations along a circular route,
where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i]
of gas to travel from station i to its next station (i+1).
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel
around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
'''

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = len(gas) - 1
        end = 0
        total = gas[start] - cost[start]
        while start > end:
            if total >= 0:
                total += gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                total += gas[start] - cost[start]
        return start if total >= 0 else -1
