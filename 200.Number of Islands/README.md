典型的DFS的题目，因为岛要与其他的’1’相连。

需要注意的是走过的地方就赋值为’0’，当然也可以赋值为其他值，判断的时候判断不为‘1’即可。

为了推出dfs也为了下次在当前值为’1’时调用dfs时的计数加1是准确的。

submit的结果为:
```
45 / 45 test cases passed.
Status: Accepted
Runtime: 124 ms
```

第二版用了BFS，就是把上一版的DFS函数换为BFS。

BFS函数在进入时将该点的坐标压入queue，并将其值赋为’0’。

然后把上下左右为’1’的压入queue，并将其值赋为’0‘。

循环到quue为空为止。

submit的结果为:
```
45 / 45 test cases passed.
Status: Accepted
Runtime: 108 ms
```
