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
        step = 0
        ladder = {}
        for word in wordlist:
            ladder[word] = 2 ** 31 - 1
        ladder[beginWord] = 0
        ladder[endWord] = 2 ** 31 - 1
        q = [beginWord]
        minStep = 2 ** 31 - 1
        linked = {}
        results = []
        while q:
            cur = q.pop(0)
            step = ladder[cur] + 1
            if step > minStep:
                break
            for i in range(len(cur)):
                for c in range(ord('a'), ord('z') + 1):
                    ch = chr(c)
                    new = cur[:i] + ch + cur[i+1:]
                    if new in ladder:
                        if step > ladder[new]:
                            continue
                        if step < ladder[new]:
                            q.append(new)
                            ladder[new] = step
                        if new in linked:
                            linked[new].append(cur)
                        else:
                            linked[new] = [cur]
                        if new == endWord:
                            minStep = step
        self.dfs(linked, endWord, beginWord, [endWord], results)
        return results

    def dfs(self, linked, word, start, result, results):
        if word == start:
            results.append(result)
            return
        if word in linked:
            for node in linked[word]:
                self.dfs(linked, node, start, [node] + result, results)
