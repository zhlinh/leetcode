#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import NumArray

nums = [1, 3, 5]
numArray = NumArray(nums)
print(numArray.sumRange(0, 2))
numArray.update(0, 2)
print(numArray.sumRange(0, 2))
print(numArray.sumRange(0, 5))
