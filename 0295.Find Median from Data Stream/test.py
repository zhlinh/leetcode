#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import MedianFinder

mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())
mf.addNum(3)
print(mf.findMedian())
