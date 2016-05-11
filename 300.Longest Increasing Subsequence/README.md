很容易想到DP的方法，但dp[i]的赋值依据不是dp[i-1]。

而是之前的每一个比nums[i]小的nums[j]所对应的dp[j]。

dp[i] = max(dp[i], dp[j] + 1)，其中j由nums[j] < nums[i], j < i限定。

时间复杂度为O(n^2)。

submit的结果为:
```
22 / 22 test cases passed.
Status: Accepted
Runtime: 1628 ms
```
