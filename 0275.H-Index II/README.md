就是二分法查找。

查找从左往右第一个citations[mid] >= n - mid的。

最后返回n-r即为所求。

此处没有把等于给单独列出来，比较容易理解。

也可以在等于的情况下直接返回n-mid。因为再往右无意义，因为n-mid值更小了，
而再往左不可能找到符合条件的了，因为n-mid变大，
而citations[mid]往左时在减小或不变(考虑重复的值)。

submit的结果为:
```
82 / 82 test cases passed.
Status: Accepted
Runtime: 116 ms
```
