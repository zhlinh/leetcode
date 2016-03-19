#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import LRUCache
from solution import DLinkNode

lru = LRUCache(3)
lru.set(1, 1)
lru.set(2, 2)
lru.set(3, 3)
lru.set(4, 4)
print(lru.get(4))
print(lru.get(3))
print(lru.get(2))
print(lru.get(1))
lru.set(5, 5)
print(lru.get(1))
print(lru.get(2))
print(lru.get(3))
print(lru.get(4))
print(lru.get(5))
