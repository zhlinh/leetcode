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
        index = [0] * len(primes)
        ugly = [1] * n
        for i in range(1, n):
            minProduct = 2 ** 31 - 1
            for j in range(len(index)):
                tmp = ugly[index[j]] * primes[j]
                if tmp <= minProduct:
                    minProduct = tmp
            for j in range(len(index)):
                if ugly[index[j]] * primes[j] == minProduct:
                    index[j] += 1
            ugly[i] = minProduct
        return ugly[n-1]
