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
        q = [beginWord]
        linked = {}
        results = []
        visited = set()
        unvisited = set(wordlist)
        unvisited.add(endWord)
        unvisited.discard(beginWord)
        found = False
        while q:
            width = len(q)
            for _ in range(width):
                cur = q.pop(0)
                for i in range(len(cur)):
                    for c in range(ord('a'), ord('z') + 1):
                        ch = chr(c)
                        new = cur[:i] + ch + cur[i+1:]
                        if new in unvisited:
                            # in a level only distinct node,
                            # so do not add the same node to queue
                            if new not in visited:
                                visited.add(new)
                                q.append(new)
                            # But a node can link to many prev nodes
                            if new in linked:
                                linked[new].append(cur)
                            else:
                                linked[new] = [cur]
                            if new == endWord:
                                found = True
            if found:
                break
            for vi in visited:
                unvisited.discard(vi)
            visited = set()
        self.dfs(linked, endWord, beginWord, [endWord], results)
        return results

    def dfs(self, linked, word, start, result, results):
        if word == start:
            results.append(result)
            return
        if word in linked:
            for node in linked[word]:
                self.dfs(linked, node, start, [node] + result, results)
