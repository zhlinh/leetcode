用了一个HashSet。时间复杂度为O(n)。

另外的方法还有O(n^2)的，还有先排序后查找的O(nlog(n))的。

对于python还可以用一行代码return len(nums) > len(set(nums))。

submit的结果为:
```
16 / 16 test cases passed.
Status: Accepted
Runtime: 60 ms
```
