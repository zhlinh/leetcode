#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
#  preorder = "1,#"
#  preorder = "1,#,2,#,#"
#  preorder = "9,#,#,1"
sol = Solution()
res = sol.isValidSerialization(preorder)
print(res)
