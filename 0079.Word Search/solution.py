#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-29
Last_modify:    2016-02-29
******************************************
'''

'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) < 1:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False

    def dfs(self, board, word, posi, posj, start):
        if start >= len(word):
            return True
        if posi < 0 or posi >= len(board) or posj < 0 or posj >= len(board[0]):
            return False
        if board[posi][posj] != word[start]:
            return False
        board[posi][posj] = 0
        res = self.dfs(board, word, posi + 1, posj, start + 1) \
              or self.dfs(board, word, posi - 1, posj, start + 1) \
              or self.dfs(board, word, posi, posj + 1, start + 1) \
              or self.dfs(board, word, posi, posj - 1, start + 1)
        board[posi][posj] = word[start]
        return res
