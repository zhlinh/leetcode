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
        unvisited = set(wordList)
        unvisited.discard(endWord)
        unvisited.discard(beginWord)
        charSet = "abcdefghijklmnopqrstuvwxyz"
        level = 0
        front = set([beginWord])
        back = set([endWord])
        while front:
            visited = set()
            level += 1
            for cur in front:
                for i in range(len(cur)):
                    for ch in charSet:
                        new = cur[:i] + ch + cur[i+1:]
                        # IF there is common word, connected
                        if new in back:
                            return level + 1
                        if new in unvisited:
                            visited.add(new)
            front = visited
            print(front, back)
            if len(front) > len(back):
                front, back = back, front
            unvisited -= visited
        return 0
