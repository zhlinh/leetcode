第一步先将nums转换为set，然后以前面无连续元素的当前元素往后查找元素得出长度。

因为set是以hash的方式存储所以查找的复杂度可以降为O(n)。

才有时间复杂度为O(n)。

submit的结果为:
```
67 / 67 test cases passed.
Status: Accepted
Runtime: 60 ms
```

第二版用了dict，存放的是当前连续的长度。

计算长度的方法为dict[n] = dict[n-1] + dict[n+1] + 1。

然后更新左右两端的长度。

值得注意的是遇到重复元素时应不处理，否则长度会翻倍。

submit的结果为:
```
67 / 67 test cases passed.
Status: Accepted
Runtime: 60 ms
```
