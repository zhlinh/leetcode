第一版用的是DP的方法。

到当前层除首尾外的dp[i] = min(dp[i], dp[i-1]) + 当前元素

如果是首尾因为只有一条路径，所以再加上当前元素即可。

```
43 / 43 test cases passed.
Status: Accepted
Runtime: 68 ms
```
