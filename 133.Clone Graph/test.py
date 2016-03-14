#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution
from solution import UndirectedGraphNode

def mkUdGraph(s):
    dic = {}
    node, neib = None, None
    root = None
    flag = 1
    for ob in s.split('#'):
        ob = ob.strip()
        x = ob.split(',')
        for i in range(len(x)):
            if i == 0:
                if x[i] not in dic:
                    node = UndirectedGraphNode(x[i])
                    dic[x[i]] = node
                else:
                    node = dic[x[i]]
                if flag:
                    root = node
                    flag = 0
            else:
                if x[i] not in dic:
                    neib = UndirectedGraphNode(x[i])
                    dic[x[i]] = neib
                else:
                    neib = dic[x[i]]
                node.neighbors.append(neib)
    return root

def lsUdGraph(node):
    if not node:
        return ""
    visited = set()
    q = [node]
    res = []
    while q:
        new = q.pop(0)
        visited.add(new.label)
        tmp = []
        tmp.append(str(new.label))
        for neib in new.neighbors:
            tmp.append(str(neib.label))
            if neib.label not in visited:
                q.append(neib)
                visited.add(neib.label)
        res.append(','.join(tmp))
    print('#'.join(res))


node = mkUdGraph("0,1,2#1,2#2,2")
sol = Solution()
res = sol.cloneGraph(node)
lsUdGraph(res)
