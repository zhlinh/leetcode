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
        return self.dfs(self.root, word, 0)

    def dfs(self, node, word, i):
        if i >= len(word):
            return node.isWord
        if word[i] == '.':
            for child in node.children:
                if self.dfs(node.children[child], word, i + 1):
                    return True
            return False
        else:
            if word[i] not in node.children:
                return False
            return self.dfs(node.children[word[i]], word, i + 1)

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
