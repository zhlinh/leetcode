#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-20
Last_modify:    2016-02-20
******************************************
'''

'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard
such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of
the n-queens' placement, where 'Q' and '.' both indicate
a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ass_col = [0 for _ in range(n)]
        ass_dia45 = [0 for _ in range(2 * n)]
        ass_dia135 = [0 for _ in range(2 * n)]
        res = []
        results = []
        self.solve(results, res, ass_col, ass_dia45, ass_dia135, 0, n)
        return results

    def solve(self, results, res, ass_col, ass_dia45, ass_dia135, row, n):
        if row == n:
            results.append(res)
            return
        for col in range(n):
            if not (ass_col[col] or ass_dia45[row+col] \
                    or ass_dia135[n-1+row-col]):
                tmp = '.' * col + 'Q' + '.' * (n - col - 1)
                ass_col[col] = ass_dia45[row+col] = ass_dia135[n-1+row-col] = 1
                self.solve(results, res + [tmp], ass_col, ass_dia45, ass_dia135, row + 1, n)
                ass_col[col] = ass_dia45[row+col] = ass_dia135[n-1+row-col] = 0
