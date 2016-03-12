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
Given two words (beginWord and endWord),
and a dictionary's word list, find the length
of shortest transformation sequence from beginWord to endWord, such that:
Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
'''

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        q = set([beginWord])
        visited = set()
        unvisited = set(wordList)
        unvisited.add(endWord)
        unvisited.discard(beginWord)
        level = 0
        while q:
            level += 1
            for cur in q:
                for i in range(len(cur)):
                    for c in range(ord('a'), ord('z') + 1):
                        ch = chr(c)
                        new = cur[:i] + ch + cur[i+1:]
                        if new == endWord:
                                return level + 1
                        if new in unvisited:
                            visited.add(new)
            unvisited -= visited
            q = visited
            visited = set()
        return 0
