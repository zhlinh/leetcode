和计算最大的矩形面积基本方法是一样的，仅需要取高和长的最小值作为边长即可。

用了三个dp数组，分别作为height，left，right。

注意计算right时需要从右往左循环。

left和right从上一次的值和前一个值的较大值和较小值得出。

submit的结果为:
```
67 / 67 test cases passed.
Status: Accepted
Runtime: 172 ms
```

第二版也是DP，但运用了更简单的DP规则。

当当前元素为1时，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1。

即dp[i][j]为右下角元素的dp值由左上的三个元素dp值的最小值然后加1决定。

submit的结果为:
```
67 / 67 test cases passed.
Status: Accepted
Runtime: 120 ms
```
