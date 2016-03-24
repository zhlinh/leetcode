典型的dfs的题目，因为岛要与其他的’1’相连。

需要注意的是走过的地方就赋值为’0’。

为了推出dfs也为了下次在当前值为’1’时调用dfs时的计数加1是准确的。

submit的结果为:
```
45 / 45 test cases passed.
Status: Accepted
Runtime: 124 ms
```
