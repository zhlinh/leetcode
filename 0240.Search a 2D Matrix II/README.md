挺有意思的题目。

关键要懂得搜索从何开始，才能让target大于、小于、等于当前值时有理性的移动。

选择`右上角`开始，这样target大于时，row往下移。target小于时，col往右移。
等于时就返回True。

时间复杂度为O(m + n)。

当然也可以在每一行用二分法，这样的时间复杂度为O(mlog(n))。

submit的结果为:
```
127 / 127 test cases passed.
Status: Accepted
Runtime: 116 ms
```
