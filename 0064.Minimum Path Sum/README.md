第一版用了DP，核心思想为:

    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

时间复杂度为O(n * m)。

submit的结果为:
```
61 / 61 test cases passed.
Status: Accepted
Runtime: 68 ms
```
