用的DP的思想。

就是一个数可以表示成某个数加上j*j。

这样就是dp[i] = min(dp[i], dp[i-j*j] + 1)。

dp[i]表示平方数的个数。

之所以用到静态变量，是因为多次调用时可以用之前的结果。

即只要是小于当前dp长度的，直接返回dp[n]即可。

否则逐一往下计算dp值。

时间复杂度为O(n^2)。

submit的结果为:
```
600 / 600 test cases passed.
Status: Accepted
Runtime: 332 ms
```
