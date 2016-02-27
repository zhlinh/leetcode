#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-26
Last_modify:    2016-02-26
******************************************
'''

'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
'''

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return ""
        tmp = ""
        res = []
        path = path + "/"
        for i in range(len(path)):
            if path[i] == '/':
                if tmp == "" or tmp == ".":
                    tmp = ""
                    continue
                if tmp == "..":
                    if len(res) > 0:
                        res.pop()
                else:
                    res.append(tmp)
                tmp = ""
            else:
                tmp += path[i]
        return "/" + '/'.join(res)
