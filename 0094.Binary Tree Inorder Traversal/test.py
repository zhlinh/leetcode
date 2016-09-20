#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution
from solution import TreeNode


def constructOne(s):
    if s == '#':
        return None
    else:
        return TreeNode(int(s))

def createTree(tree):
    q = []
    root = constructOne(tree[0]);
    q.append(root);
    idx = 1;
    while q:
        tn = q.pop(0)
        if not tn:
            continue
        if idx == len(tree):
            break
        left = constructOne(tree[idx])
        tn.left = left
        q.append(left)
        idx += 1
        if idx == len(tree):
            break
        right = constructOne(tree[idx])
        idx += 1
        tn.right = right
        q.append(right)
    return root

#  inpt = createTree(['1', '#', '2', '3'])
inpt = createTree(['1', '2', '3', '#' , '#', '4', '#', '#', '5'])
sol = Solution()
res = sol.inorderTraversal(inpt)
print(res)
