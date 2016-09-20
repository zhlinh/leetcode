#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-16
Last_modify:    2016-05-16
******************************************
'''

'''
For a undirected graph with tree characteristics,
we can choose any node as the root.
The result graph is then a rooted tree.
Among all possible rooted trees,
those with minimum height are called minimum height trees (MHTs).
Given such a graph, write a function to find all the MHTs
and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1.
You will be given the number n and a list of undirected edges
(each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0]
and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

Hint:

How many MHTs can a graph have at most?
Note:

(1) According to the definition of tree on Wikipedia:
“a tree is an undirected graph in which any two vertices
are connected by exactly one path. In other words,
any connected graph without simple cycles is a tree.”

(2) The height of a rooted tree is the number of edges
on the longest downward path between the root and a leaf.

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
'''

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        nodes = [[] for _ in range(n)]
        leaves = []
        for a, b in edges:
            nodes[a].append(b)
            nodes[b].append(a)
        for i in range(n):
            if len(nodes[i]) == 1:
                leaves.append(i)
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for leaf in leaves:
                nextNode = nodes[leaf].pop()
                nodes[nextNode].remove(leaf)
                if len(nodes[nextNode]) == 1:
                    newLeaves.append(nextNode)
            leaves = newLeaves
        return leaves
