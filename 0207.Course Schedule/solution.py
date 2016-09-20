#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-24
Last_modify:    2016-03-24
******************************************
'''

'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites,
for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take.
To take course 1 you should have finished course 0,
and to take course 0 you should also have finished course 1.
So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges,
not adjacency matrices. Read more about how a graph is represented.

Hints:
1. This problem is equivalent to finding if a cycle exists in a directed graph.
   If a cycle exists, no topological ordering exists and therefore it
2. will be impossible to take all courses.
   Topological Sort via DFS - A great video tutorial (21 minutes)
   on Coursera explaining the basic concepts of Topological Sort.
3. Topological sort could also be done via BFS.
'''

from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        matrix = [set() for _ in range(numCourses)]
        for p in prerequisites:
            matrix[p[1]].add(p[0])
        visited = [0] * numCourses
        for i in range(numCourses):
            if visited[i] == 0:
                if not self.dfs(matrix, i, visited):
                    return False
        return True

    def dfs(self, matrix, i, visited):
        visited[i] = 1
        for neighbor in matrix[i]:
            if visited[neighbor] == 1:
                return False
            if visited[neighbor] == 0 and not self.dfs(matrix, neighbor, visited):
                return False
        visited[i] = -1
        return True
