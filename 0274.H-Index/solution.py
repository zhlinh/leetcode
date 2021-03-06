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
Given an array of citations (each citation is a non-negative integer) of
a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has
index h if h of his/her N papers have at least h citations each,
and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the
researcher has 5 papers in total and each of them had
received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations
each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h,
the maximum one is taken as the h-index.

Hint:

An easy approach is to sort the array first.
What are the possible values of h-index?
A faster approach is to use extra space.
Credits:
Special thanks to @jianchao.li.fighter for adding this problem
and creating all test cases.
'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n == 0:
            return 0
        count = [0] * (n + 1)
        total = 0
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1
        for i in reversed(range(n + 1)):
            total += count[i]
            if total >= i:
                return i
        return 0

