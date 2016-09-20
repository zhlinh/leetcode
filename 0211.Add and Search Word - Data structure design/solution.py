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
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular
expression string containing only letters a-z or .. A .
means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

click to show hint.

You should be familiar with how a Trie works.
If not, please work on this problem: Implement Trie (Prefix Tree) first.
'''

from collections import deque

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isWord = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        q = deque()
        q.append(self.root)
        i = 0
        while q and i < len(word):
            width = len(q)
            for j in range(width):
                cur = q.popleft()
                if word[i] == '.':
                    for w in cur.children:
                        q.append(cur.children[w])
                else:
                    if word[i] in cur.children:
                        q.append(cur.children[word[i]])
            i += 1
        while q:
            cur = q.popleft()
            if cur.isWord:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
