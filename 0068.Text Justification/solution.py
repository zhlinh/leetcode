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
        nw = 0
        start = 0
        cur, res = [], []
        for word in words:
            if len(cur) + nw + len(word) > maxWidth:
                if len(cur) == 0:
                    continue
                elif len(cur) == 1:
                    res.append(cur[0] + ' '*(maxWidth - nw))
                else:
                    evenSpace = (maxWidth - nw) // (len(cur) - 1)
                    extraSpace = (maxWidth - nw) % (len(cur) - 1)
                    for i in range(extraSpace):
                        cur[i] += ' '
                    res.append((' '*evenSpace).join(cur))
                nw = 0
                cur = []
            cur.append(word)
            nw += len(word)
        res.append(' '.join(cur) + ' '*(maxWidth - (nw + len(cur) - 1)))
        return res
