#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution
from solution import TreeNode

def constructOne(s):
    s = s.strip()
    if s == '#':
        return None
    else:
        return TreeNode(int(s))

def createTree(tree, val1, val2):
    q = []
    ret1, ret2 = None, None
    tree = tree.split(",")
    root = constructOne(tree[0]);
    if root and val1 == root.val:
        ret1 = root
    if root and val2 == root.val:
        ret2 = root
    q.append(root);
    idx = 1;
    while q:
        tn = q.pop(0)
        if not tn:
            continue
        if idx == len(tree):
            break
        left = constructOne(tree[idx])
        if left and val1 == left.val:
            ret1 = left
        if left and val2 == left.val:
            ret2 = left
        tn.left = left
        q.append(left)
        idx += 1
        if idx == len(tree):
            break
        right = constructOne(tree[idx])
        if right and val1 == right.val:
            ret1 = right
        if right and val2 == right.val:
            ret2 = right
        idx += 1
        tn.right = right
        q.append(right)
    return root, ret1, ret2

def printNode(tn, indent):
    sb = ""
    for i in range(indent):
        sb += "\t"
    sb += str(tn.val)
    print(sb)

def printTree(root, indent):
    if not root:
        return
    printTree(root.right, indent + 1)
    printNode(root, indent)
    printTree(root.left, indent + 1)

root, p, q = createTree("6, 2, 8, 0, 4, 7, 9, #, #, 3, 5", 2, 8)
sol = Solution()
res = sol.lowestCommonAncestor(root, p, q)
print(res.val)
