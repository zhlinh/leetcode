第一版用了类DP的方法，但在空间存储时采取了邻接列表的方式。

dp邻接列表存储的是以i为起点的回文字符串的终点j。

然后将这个邻接列表用dfs的方法得出所有组合。

当然直接dfs不用邻接列表也是可以的。

sumbmit的结果为:
```
21 / 21 test cases passed.
Status: Accepted
Runtime: 140 ms
```
