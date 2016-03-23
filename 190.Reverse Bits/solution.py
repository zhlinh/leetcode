#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-23
Last_modify:    2016-03-23
******************************************
'''

'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596
(represented in binary as 00000010100101000001111010011100),
return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

class Solution(object):
    dic = {}
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.dic:
            return self.dic[n]
        res = 0
        for i in range(32):
            res <<= 1
            res |= n & 1
            n >>= 1
        self.dic[n] = res
        return res
