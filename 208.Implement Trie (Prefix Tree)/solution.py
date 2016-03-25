#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-25
Last_modify:    2016-03-25
******************************************
'''

'''
Implement a trie with insert, search, and  methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''

class TrieNode(object):
    def __init__(self, ch = None):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.val = ch
        self.isWord = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            index = ord(ch)-ord('a')
            if node.children[index] == None:
                node.children[index] = TrieNode(ch)
            node = node.children[index]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            index = ord(ch)-ord('a')
            if node.children[index] == None:
                return False
            node = node.children[index]
        return node.isWord


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            index = ord(ch)-ord('a')
            if node.children[index] == None:
                return False
            node = node.children[index]
        return True


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
