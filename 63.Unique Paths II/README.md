第一版用了DP，核心思想为:

    dp[i][j] = dp[i-1][j] + dp[i][j-1]

即到当前位置的解法数为前一步的解法数之和。i或j为0时dp[i][j] = 1

然后如果obstacleGrid[i][j]为1时，dp[i][j] = 0

时间复杂度为O(n * m)。

submit的结果为:
```
43 / 43 test cases passed.
Status: Accepted
Runtime: 56 ms
```
