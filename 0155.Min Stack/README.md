用了一个链表来实现。

主要难度体现在如何getMin。

维护一个min值，因为一个阶段内min值只有一个。

故存入链表(即压入堆栈)的值存入的是x - min。

然后更新当前min值。

取出的时候如果值小于0，则返回min，否则返回val + min。

当然也可以用另外一个堆栈minStack来保存最小值，即用两个栈来实现。

push只需要压入小于等于当前minStack栈顶元素的值，或minStack为空时压入即可。

pop的时候当两个栈顶相等时才pop另一个堆栈minStack。

push，pop，top最后都是调用原Stack的方法。

只有getMin的时候返回的是minStack的栈顶元素。

submit的结果为:
```
17 / 17 test cases passed.
Status: Accepted
Runtime: 116 ms
```
