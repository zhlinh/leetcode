#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-10
Last_modify:    2016-05-10
******************************************
'''

'''
According to the Wikipedia's article: "The Game of Life,
also known simply as Life, is a cellular automaton devised
by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1)
or dead (0). Each cell interacts with its eight neighbors (horizontal,
vertical, diagonal) using the following four rules (taken from the above
Wikipedia article):

Any live cell with fewer than two live neighbors dies,
as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell,
as if by reproduction.
Write a function to compute the next state (after one update)
of the board given its current state.

Follow up:
Could you solve it in-place? Remember that the board needs to be updated
at the same time: You cannot update some cells first and then use their
updated values to update other cells.
In this question, we represent the board using a 2D array. In principle,
the board is infinite, which would cause problems when the active area
encroaches the border of the array. How would you address these problems?
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and
creating all test cases.
'''

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                lives = self.countLiveNeighbors(board, m, n, i, j)
                if lives == 3 or (board[i][j] and lives == 2):
                    board[i][j] |= 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

    def countLiveNeighbors(self, board, m, n, i, j):
        lives = 0
        for x in range(max(i-1, 0), min(i+2, m)):
            for y in range(max(j-1, 0), min(j+2, n)):
                lives += board[x][y] & 1
        lives -= board[i][j]
        return lives
