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
        dic_hor = [{} for _ in range(9)]
        dic_ver = [{} for _ in range(9)]
        dic_cell = [[{} for _ in range(3)] for __ in range(3)]
        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == '.':
                    continue
                if ch not in dic_hor[i]:
                    dic_hor[i][ch] = 1
                else:
                    return False
                if ch not in dic_ver[j]:
                    dic_ver[j][ch] = 1
                else:
                    return False
                if ch not in dic_cell[i//3][j//3]:
                    dic_cell[i//3][j//3][ch] = 1
                else:
                     return False
        return True
