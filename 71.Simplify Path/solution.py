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
        if len(path) < 2:
            return path
        tmp = ""
        res = []
        for i in range(len(path)):
            if path[i] == '/':
                #  print(tmp)
                if tmp == "/..":
                    if res:
                        res.pop()
                elif tmp and tmp != "/." and tmp != "/":
                    res.append(tmp)
                tmp = ""
            tmp += path[i]
        if tmp == "/..":
            if res:
                res.pop()
        elif tmp and tmp != "/" and tmp != "/.":
            res.append(tmp)
        if not res:
            return '/'
        return ''.join(res)