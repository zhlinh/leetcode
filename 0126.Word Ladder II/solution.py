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
and a dictionary's word list, find all shortest
transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
'''

class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        linked = {}
        results = []
        unvisited = set(wordlist)
        unvisited.discard(endWord)
        unvisited.discard(beginWord)
        found = False
        front = set([beginWord])
        back = set([endWord])
        charSet = "abcdefghijklmnopqrstuvwxyz"
        isFrontHead = True
        while front:
            visited = set()
            for cur in front:
                for i in range(len(cur)):
                    for ch in charSet:
                        new = cur[:i] + ch + cur[i+1:]
                        if new in back:
                            found = True
                            self.addLink(linked, isFrontHead, cur, new)
                        if not found and new in unvisited:
                            visited.add(new)
                            self.addLink(linked, isFrontHead, cur, new)
            if found:
                break
            front = visited
            if len(front) > len(back):
                front, back = back, front
                isFrontHead = not isFrontHead
            for vi in visited:
                unvisited.discard(vi)
            #  unvisited -= visited
        self.dfs(linked, endWord, beginWord, [endWord], results)
        return results

    def addLink(self, linked, isFrontHead, cur, new):
        if isFrontHead:
            if new in linked:
                linked[new].append(cur)
            else:
                linked[new] = [cur]
        else:
            if cur in linked:
                linked[cur].append(new)
            else:
                linked[cur] = [new]

    def dfs(self, linked, word, start, result, results):
        if word == start:
            results.append(result)
            return
        if word in linked:
            for node in linked[word]:
                self.dfs(linked, node, start, [node] + result, results)
