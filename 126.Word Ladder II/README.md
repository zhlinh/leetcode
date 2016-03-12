这一题花了近一天的时间，上一次有这种感觉是strStr的KMP算法。

解法是先BFS，然后从end开始DFS。

BFS用了一个step来限制深度，用了一个dict来记录前序节点，构建图。

每次只改变当前节点的某个位置的字母，然后查询是否在dictList中以确定下一跳。

构建完图后就可以用DFS从后往前增加节点。

submit的结果为:
```
37 / 37 test cases passed.
Status: Accepted
Runtime: 860 ms
```
