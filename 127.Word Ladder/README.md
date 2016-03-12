第一版用了unvisited和visited两个set来构建图。BFS。

本层中不能重复有之前的节点。

本层的节点都是不同的，注意不要往queue中重复添加相同节点。但可连接多个前序节点。

然后返回当前层数 + 1(因为最后的endWord也算一层)。

submit的结果为:
```
37 / 37 test cases passed.
Status: Accepted
Runtime: 820 ms
```
