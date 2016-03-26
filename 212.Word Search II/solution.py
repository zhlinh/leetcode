#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-26
Last_modify:    2016-03-26
******************************************
'''

'''
Given a 2D board and a list of words from the dictionary,
find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.

click to show hint.

You would need to optimize your backtracking to pass the larger test.
Could you stop backtracking earlier?

If the current candidate does not exist in all words' prefix,
you could stop backtracking immediately.
What kind of data structure could answer such query efficiently?
Does a hash table work? Why or why not? How about a Trie?
If you would like to learn how to implement a basic trie,
please work on this problem: Implement Trie (Prefix Tree) first.
'''

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.word = None

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
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m = len(board)
        if m < 1:
            return []
        n = len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        node = trie.root
        results = []
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, node, results)
        return results

    def dfs(self, board, i, j, node, results):
        if node.word:
            results.append(node.word)
            node.word = None
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        c = board[i][j]
        if c == '#':
            return
        node = node.children.get(c, None)
        if not node:
            return
        board[i][j] = '#'
        self.dfs(board, i+1, j, node, results)
        self.dfs(board, i-1, j, node, results)
        self.dfs(board, i, j+1, node, results)
        self.dfs(board, i, j-1, node, results)
        board[i][j] = c
