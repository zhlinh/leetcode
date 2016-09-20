#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Codec
from solution import TreeNode

def createNode(s):
    s = s.strip()
    if s == '#':
        return None
    else:
        return TreeNode(int(s))

def createTree(data):
    q = []
    data = data.split(",")
    root = createNode(data[0]);
    q.append(root);
    idx = 1;
    while q:
        cur = q.pop(0)
        if idx == len(data):
            break
        cur.left = createNode(data[idx])
        if cur.left:
            q.append(cur.left)
        idx += 1
        if idx == len(data):
            break
        cur.right = createNode(data[idx])
        if cur.right:
            q.append(cur.right)
        idx += 1
    return root

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

root = createTree("1, 2, 3, #, #, 4, 5")
data = [0,0,0,0,None,None,1,None,None,None,2]
#  data = [None]
sol = Codec()
seri = sol.serialize(root)
print(seri)
deseri = sol.deserialize(data)
print(printTree(deseri, 0))
