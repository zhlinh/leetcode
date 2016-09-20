这一题花了近一天的时间，上一次有这种感觉是strStr的KMP算法。

解法是先BFS，然后从end开始DFS。

BFS用了一个step来限制深度，用了一个dict来记录前序节点，构建图。

每次只改变当前节点的某个位置的字母，然后查询是否在dictList中以确定下一跳。

使用了step与ladder里存的step值不相等来避免添加本层重复元素。

利用step小于ladder里存的step值[初始化为int的最大值]来避免添加之前的重复元素。

构建完图后就可以用DFS从后往前增加节点。

submit的结果为:
```
37 / 37 test cases passed.
Status: Accepted
Runtime: 860 ms
```

第二版用了unvisited和visited两个set来构建图。其他和第一版的思路是一样的。

本层中不能重复有之前的节点。

本层的节点都是不同的，注意不要往queue中重复添加相同节点。但可连接多个前序节点。

submit的结果为:
```
37 / 37 test cases passed.
Status: Accepted
Runtime: 808 ms
```

第三版用了双向BFS(bidirectional BFS)。

需要注意的是正向和反向时linked邻接节点列表的添加的不同。

其实就是节点和下一跳位置会颠倒。

另外需要注意的是当两锋面相接时应作为另外的情况考虑。

将锋面连起来，而不是还在寻找unvisited的节点。

速度要比普通BFS要快的多。

submit的结果为:
```
37 / 37 test cases passed.
Status: Accepted
Runtime: 128 ms
```
