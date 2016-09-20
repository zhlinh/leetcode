#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import NumArray

nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)
print(numArray.sumRange(0, 2))
print(numArray.sumRange(2, 5))
print(numArray.sumRange(0, 5))
