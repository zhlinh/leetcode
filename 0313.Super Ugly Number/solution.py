#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-16
Last_modify:    2016-05-16
******************************************
'''

'''
Write a program to find the n-th super ugly number.

Super ugly numbers are positive numbers whose all prime factors are
in the given prime list primes of size k.
For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
is the sequence of the first 12 super ugly numbers given
primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
'''

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import heapq
        q = []
        uglyNums = [1] * n
        k = len(primes)
        for i in range(k):
            heapq.heappush(q, (primes[i], 0, primes[i]))
        for ui in range(1, n):
            val, index, prime = q[0]
            uglyNums[ui] = val
            while q and q[0][0] == val:
                val, index, prime = heapq.heappop(q)
                heapq.heappush(q, (prime * uglyNums[index+1], index+1, prime))
        return uglyNums[n-1]
