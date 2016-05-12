#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-12
Last_modify:    2016-05-12
******************************************
'''

'''
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers.
Except for the first two numbers, each subsequent number
in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence:
1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros,
so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9',
write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?

Credits:
Special thanks to @jeantimex for adding this problem and creating all test cases.
'''

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range(n // 2 + 1):
            if num[0] == '0' and i != 0:
                break
            for j in range(i+1, n - 1):
                if num[i+1] == '0' and j != i+1:
                    break
                if self.isValid(num, i, j):
                    return True
        return False

    def isValid(self, num, i, j):
        a = int(num[:i+1])
        b = int(num[i+1:j+1])
        start = j + 1
        while start < len(num):
            a = a + b
            if num[start] == '0' and a != 0:
                return False
            sa = str(a)
            # check overflow
            if not num.startswith(sa, start):
                return False
            if sa == num[start:start+len(sa)]:
                a, b = b, a
                start += len(sa)
            else:
                return False
        return True
