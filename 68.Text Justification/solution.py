#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-25
Last_modify:    2016-02-25
******************************************
'''

'''
Given an array of words and a length L,
format the text such that each line has
exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach;
that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary
so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words,
the empty slots on the left will be assigned
more spaces than the slots on the right.

For the last line of text,
it should be left justified and
no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
'''

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        nw, lw = 0, 0
        start = 0
        curWidth = 0
        res = []
        for i in range(len(words)):
            nw += 1
            lw += len(words[i])
            curWidth = lw + nw -1
            if curWidth > maxWidth:
                lastWidth = curWidth - len(words[i]) - 1
                self.addLine(words, maxWidth, lastWidth, nw - 1, start, i - 1, res)
                start = i
                nw, lw = 1, len(words[i])
        self.addLine(words, maxWidth, curWidth, nw, start, len(words) - 1, res)
        return res

    def addLine(self, words, maxWidth, width, nw, start, end, res):
        if end != len(words) - 1:
            evenSpace = (maxWidth - width) // (nw - (nw != 1))
            extraSpace = (maxWidth - width) % (nw - (nw != 1))
            print(evenSpace, extraSpace)
        else:
            evenSpace, extraSpace = 0, 0
        tmp = ""
        for j in range(start, end + 1):
            if j == end:
                tmp += words[j]
            elif j < start + extraSpace:
                tmp = tmp + words[j] + ' '*(evenSpace + 2)
            else:
                tmp = tmp + words[j] + ' '*(evenSpace + 1)
        tmp = tmp + ' '*(maxWidth - len(tmp))
        res.append(tmp)
