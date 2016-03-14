第一版用了DFS的方法。

从最外层的四条边向内检查如果遇到O则变为1，这样可以防止回溯，否则就会一直在检查O。

然后就是把1变为O，把O变为X即为题中所求。

比较tricky的是，判断往内部dfs是用的边界判定是：

    if i > 1:
    if i < m - 2:

这样可以避免重复检查边界，提高运行效率，避免LTE。

sumbmit的结果为:
```
58 / 58 test cases passed.
Status: Accepted
Runtime: 160 ms
```
