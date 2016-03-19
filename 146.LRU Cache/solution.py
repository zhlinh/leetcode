#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-18
Last_modify:    2016-03-18
******************************************
'''

'''
Design and implement a data structure for
Least Recently Used (LRU) cache.
It should support the following operations: get and set.

get(key) - Get the value (will always be positive)
of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is
not already present. When the cache reached its capacity,
it should invalidate the least recently used item
before inserting a new item.
'''

class DLinkNode(object):
    def __init__(self):
        self.key = 0
        self.value = 0
        self.pre = None
        self.post = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.count = 0
        self.capacity = capacity
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.post = self.tail
        self.tail.pre = self.head

    def addNode(self, node):
        node.pre = self.head
        node.post = self.head.post
        self.head.post.pre = node
        self.head.post = node

    def removeNode(self, node):
        node.pre.post = node.post
        node.post.pre = node.pre

    def moveToHead(self, node):
        self.removeNode(node)
        self.addNode(node)

    def popTail(self):
        res = self.tail.pre
        self.removeNode(res)
        return res

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        else:
            newNode = DLinkNode()
            newNode.key = key
            newNode.value = value
            self.cache[key] = newNode
            self.addNode(newNode)
            self.count += 1
            if self.count > self.capacity:
                self.cache.pop(self.popTail().key, None)
                self.count -= 1
