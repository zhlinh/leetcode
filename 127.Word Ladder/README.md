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

第二版用了双向BFS，这就一下速度就提上来了，因为当前层的节点越多，就越慢。

如果只是单向，会是一个不断扩大层面的过程，直到找到endWord结束。

而双向开始，每次都找不同的节点，会在中间的时候连接起来，然后就形成了通路。

连接的条件时下一个层的元素在另一层面中存在。

front和back都表示锋面，即当前层的节点。

值得注意的是每次中间推进的时候都应该拿节点数较小的锋面推进。

这样才能够加快速度，否则和普通BFS就没有区别了。

submit的结果为:
```
37 / 37 test cases passed.
Status: Accepted
Runtime: 172 ms
```
