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
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of
the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.

Hint:

1. The naive approach is to call isUgly for every number
until you reach the n-th one.  Most numbers are not ugly.
Try to focus your effort on generating only the ugly ones.

2. An ugly number must be multiplied by either 2, 3, or 5 from
a smaller ugly number.

3. The key is how to maintain the order of the ugly numbers.
Try a similar approach of merging from three sorted lists: L1, L2, and L3.

4. Assume you have Uk, the kth ugly number.
Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''

from collections import deque

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = [1] * n
        t1, t2, t3 = 0, 0, 0
        for i in range(1, n):
            q[i] = min(q[t1] * 2, q[t2] * 3, q[t3] * 5)
            if q[i] == q[t1] * 2:
                t1 += 1
            if q[i] == q[t2] * 3:
                t2 += 1
            if q[i] == q[t3] * 5:
                t3 += 1
        return q[n-1]
