第一版用了DFS的方法。

其实也就是深度复制邻接列表。列表的每一行都是一个节点，然后会有一个neighbors数组。

为了不重复新建节点用了一个dict来存储全部节点。

需要注意的是每次返回的或加入的都应该不是原来的节点[同一索引]。

这样才达到深度复制的目的。

sumbmit的结果为:
```
12 / 12 test cases passed.
Status: Accepted
Runtime: 96 ms
```
