#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-24
Last_modify:    2016-03-24
******************************************
'''

'''

Description:

Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

Hint:

Let's start with a isPrime function. To determine if a number is prime,
we need to check if it is not divisible by any number less than n.
The runtime complexity of isPrime function would be O(n) and hence
counting the total prime numbers up to n would be O(n2). Could we do better?

Show More Hint
'''

import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        res = 1
        primes = [True] * n
        upper = math.sqrt(n)
        for i in range(3, n, 2):
            if primes[i]:
                res += 1
                if i > upper:
                    continue
                for j in range(i*i, n, i):
                    primes[j] = False
        return res
