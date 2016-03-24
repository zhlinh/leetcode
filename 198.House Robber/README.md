第一版就是DP的解法。

其核心为取之前第二个DP值和之前第三个DP值的最大值与当前nums值相加得到当前DP值。

因为可能隔两天再行动会得到更好的收益。

需要注意的是最后返回的并不是dp[n]，而是dp[n-1]和dp[n]的较大值。

因为这两个结果是独立的两条线。

submit的结果为:
```
69 / 69 test cases passed.
Status: Accepted
Runtime: 44 ms
```
