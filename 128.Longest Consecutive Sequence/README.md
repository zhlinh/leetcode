第一步先将nums转换为set，然后以前面无连续元素的当前元素往后查找元素得出长度。

因为set是以hash的方式存储所以查找的复杂度可以降为O(n)。

才有时间复杂度为O(n)。

submit的结果为:
```
67 / 67 test cases passed.
Status: Accepted
Runtime: 60 ms
```
