#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import MinStack
from solution import LinkNode

st = MinStack()
st.push(1)
st.push(2)
st.push(0)
print(st.top())
print(st.getMin())
st.pop()
print(st.getMin())
