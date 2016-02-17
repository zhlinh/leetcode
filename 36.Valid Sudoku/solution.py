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
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
[http://sudoku.com.au/TheRules.aspx]

The Sudoku board could be partially filled,
where empty cells are filled with the character '.'.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable.
Only the filled cells need to be validated.
'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            dic_hor, dic_ver = {}, {}
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in dic_hor:
                        dic_hor[board[i][j]] = 1
                    else:
                        return False
                if board[j][i] != '.':
                    if board[j][i] not in dic_ver:
                        dic_ver[board[j][i]] = 1
                    else:
                        return False
        for m in range(0, 7, 3):
            for n in range(0, 7, 3):
                dic_sub = {}
                for i in range(3):
                    for j in range(3):
                        if board[i+m][j+n] != '.':
                            if board[i+m][j+n] not in dic_sub:
                                dic_sub[board[i+m][j+n]] = 1
                            else:
                                return False
        return True
