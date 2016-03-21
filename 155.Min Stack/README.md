用了一个链表来实现。

主要难度体现在如何getMin。

维护一个min值，因为一个阶段内min值只有一个。

故存入链表(即压入堆栈)的值存入的是x - min。

然后更新当前min值。

取出的时候如果值小于0，则返回min，否则返回val + min。

当然也可以用另外一个堆栈来保存最小值，只需要压入小于等于当前最小值的即可。

pop的时候当等于的时候才pop另一个堆栈。

submit的结果为:
```
17 / 17 test cases passed.
Status: Accepted
Runtime: 116 ms
```
