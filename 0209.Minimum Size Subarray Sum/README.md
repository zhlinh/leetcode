就是求subString的常用O(n)解法。

两个循环，外层循环循环整个数组，内层循环在满足条件时进入。

内层循环将起点逐渐往后移动，缩小子数组的范围直到不满足时退出。

这样便可求得长度最小的满足条件的子数组。

submit的结果为:
```
14 / 14 test cases passed.
Status: Accepted
Runtime: 48 ms
```
