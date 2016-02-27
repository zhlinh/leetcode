#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

#  path = "/a/./b/../../c/"
path = "///"
sol = Solution()
res = sol.simplifyPath(path)
print(res)
