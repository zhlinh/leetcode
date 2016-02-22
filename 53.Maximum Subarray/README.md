第一版用的DP，但一开始会想到的是O(n^2)的解法，然后就超时了。

看了别人的答案后，才知道有一个Kadane's algorithm，太巧妙了。

算法核心是dp[i] = nums[i] if dp[i-1] < 0 else dp[i-1] + nums[i]。

时间复杂度为O(n)。

submit的结果为:
```
201 / 201 test cases passed.
Status: Accepted
Runtime: 64 ms
```
