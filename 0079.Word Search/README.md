第一版用了DFS。避免重复的方法是将当前检验过的置为0，或者别的不会出现的字母。

当前层级的dfs之后再还原回来。

submit的结果为:
```
87 / 87 test cases passed.
Status: Accepted
Runtime: 592 ms
```
