#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-11
Last_modify:    2016-03-11
******************************************
'''

'''
Given a 2D board containing 'X' and 'O',
capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's
into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m < 2:
            return
        n = len(board[0])
        for i in range(m):
            self.helper(board, i, 0, m, n)
            if n > 1:
                self.helper(board, i, n - 1, m, n)
        for j in range(n):
            self.helper(board, 0, j, m, n)
            if m > 1:
                self.helper(board, m - 1, j, m, n)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '1':
                    board[i][j] = 'O'

    def helper(self, board, i, j, m, n):
        if board[i][j] == 'O':
            board[i][j] = '1'
            # trick here, normally it could be i >= 1.
            # but the boardary will alays get checked.
            # so i == 1, then check 0 is duplicated.
            if i > 1:
                self.helper(board, i - 1, j, m, n)
            if i < m - 2:
                self.helper(board, i + 1, j, m, n)
            if j > 1:
                self.helper(board, i, j - 1, m, n)
            if j < n - 2:
                self.helper(board, i, j + 1, m, n)
