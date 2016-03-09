第一版用的是DP的方法。

到当前层除首尾外的dp[i] = min(dp[i], dp[i-1]) + 当前元素

如果是首尾因为只有一条路径，所以再加上当前元素即可。

submit的结果为:
```
43 / 43 test cases passed.
Status: Accepted
Runtime: 68 ms
```

第二版也是DP。不过是从后往前，先把最后一行存入dp。

然后再往第一层算，这样可以让代码更加简洁，不必考虑边界情况。

而且只需返回dp[0]，而不是还需计算min(dp)。


submit的结果为:
```
43 / 43 test cases passed.
Status: Accepted
Runtime: 52 ms
```
