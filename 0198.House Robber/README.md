第一版就是DP的解法。

其核心为取之前第二个DP值和之前第三个DP值的最大值与当前nums值相加得到当前DP值。

因为可能隔两家再行动会得到更好的收益。

需要注意的是最后返回的并不是dp[n]，而是dp[n-1]和dp[n]的较大值。

因为这两个结果是独立的两条线。

submit的结果为:
```
69 / 69 test cases passed.
Status: Accepted
Runtime: 44 ms
```

第二版其实也是一样的思路，只是这次只用了两个变量a和b。

O(1) space的解法，a记录的是下标为偶数的当前最大值，b记录的是下标为奇数的当前最大值。

核心是a+nums[i]与b比较取较大值。

这样就可以保证可以隔两家再行动，即a当前可以不行动，因为前面可按照b的路线。

反观b也是一样的，如果前一家收益比较多，那当前就不行动。

> 与第一版dp的区别:

第一版dp是当天一定要行动。dp[i] = max(dp[i-2], dp[i-3]) + nums[i]。

而这一版是当天可行动(如偶数天取值a+nums[i])可不行动(如偶数天取值b)。

submit的结果为:
```
69 / 69 test cases passed.
Status: Accepted
Runtime: 44 ms
```
