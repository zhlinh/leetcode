#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-17
Last_modify:    2016-02-17
******************************************
'''

'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def solve(r, c):
            """
            :type board: List[List[str]]
            :type r: int
            :type c: int
            :rtype: void Do not return anything, modify board in-place instead.
            """
            while r < 9:
                while c < 9:
                    if board[r][c] == '.':
                        cands = row[r] | col[c] | cell[r//3][c//3]
                        # 511 is b'111111111'(2^9-1)
                        if cands == 511:
                            return False
                        for num in range(9):
                            mask = 1 << num
                            if (mask & cands) == 0:
                                row[r] |= mask
                                col[c] |= mask
                                cell[r//3][c//3] |= mask
                                board[r][c] = chr(num + ord('1'))
                                if solve(r, c):
                                    return True
                                recover = ~mask
                                row[r] &= recover
                                col[c] &= recover
                                cell[r//3][c//3] &= recover
                                board[r][c] = '.'
                        return False
                    c += 1
                c = 0
                r += 1
            return True

        row = [0 for _ in range(9)]
        col = [0 for _ in range(9)]
        cell = [[0 for _ in range(3)] for __ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = ord(board[i][j]) - ord('1')
                    mask = 1 << num
                    row[i] |= mask
                    col[j] |= mask
                    cell[i//3][j//3] |= mask
        solve(0, 0)
