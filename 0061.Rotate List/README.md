第一版就直接找出新ListNode的起点和终点即可。

需要注意的是k有可能会大于ListNode的长度n。故应k = k % n。

时间复杂度为O(n)。

submit的结果为:
```
230 / 230 test cases passed.
Status: Accepted
Runtime: 52 ms
```
