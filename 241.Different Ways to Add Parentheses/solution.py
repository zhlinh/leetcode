#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-05
Last_modify:    2016-05-05
******************************************
'''

'''
Given a string of numbers and operators,
return all possible results from computing
all the different possible ways to group numbers
and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
'''

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        self.cache = {}
        return self.helper(input)

    def helper(self, input):
        if input in self.cache:
            return self.cache[input]
        if input.isdigit():
            self.cache[input] = [int(input)]
            return [int(input)]
        res = []
        for i in range(len(input)):
            c = input[i]
            if c == '+' or c == '-' or c == '*':
                res1 = self.helper(input[:i])
                res2 = self.helper(input[i+1:])
                for a in res1:
                    for b in res2:
                        if c == '+':
                            res.append(a + b)
                        elif c == '-':
                            res.append(a - b)
                        else:
                            res.append(a * b)
        #  if not res:
            #  res.append(int(input))
        self.cache[input] = res
        return res

