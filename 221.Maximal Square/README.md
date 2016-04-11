和计算最大的矩形面积基本方法是一样的，仅需要取高和长的最小值作为边长即可。

用了三个dp数组，分别作为height，left，right。

注意计算right时需要从右往左循环。

left和right从上一次的值和前一个值的较大值和较小值得出。

时间复杂度为O(nlog(n))。

submit的结果为:
```
67 / 67 test cases passed.
Status: Accepted
Runtime: 172 ms
```
