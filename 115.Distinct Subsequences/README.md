第一版用了DP的方法。

行表示s(str)，列表示t(target substr)。

第一行全部是1，表示s都会包含空substr，且仅一种情况。

第一列除(0, 0)外都为0。

然后如果`s[j-1]`和`t[i-1]`相等时:

    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

即等于s没有该字符时仅匹配到前一字符的匹配情况(必须需要该字符匹配完成)

加上s没有该字符但完成了匹配的情况(不需要该字符)。

否则:

    dp[i][j] = dp[i][j-1]

即s有没有该字符都一样的。

```
63 / 63 test cases passed.
Status: Accepted
Runtime: 180 ms
```