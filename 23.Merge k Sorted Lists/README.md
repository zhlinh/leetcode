第一版是基于合并两个ListNode的，首尾两个逐渐往中间合并，加到新的List中。

新的List大约为原长度一半大小。

然后再按此方法循环，最终得到长度为1的时候，就是合并完成的ListNode。

submit的结果为：
```
130 / 130 test cases passed.
Status: Accepted
Runtime: 172 ms
```
