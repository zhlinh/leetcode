第一版用用了merge的方法。找中点，然后将前面部分的最末的下一跳赋值为None。

用了递归所以空间复杂度为O(log(n))。

时间复杂度为O(nlog(n))。

submit的结果为:
```
15 / 15 test cases passed.
Status: Accepted
Runtime: 432 ms
```

第二版就是真正的O(1)空间，O(nlog(n))时间了。

也是merge，但用了循环，没有用递归。就是bottom-up的思路。

先将从左往右1个和1个merge，然后2个和2个...

至多会有一个(少于当前step的)落单。

所以在split(将链表按step切断)的时候要注意终止条件还有到了最末的情况。

merge还需要返回一个merge好的链表的最后一个节点作为tail。

作为下一次merge的dummy-head。

submit的结果为:
```
15 / 15 test cases passed.
Status: Accepted
Runtime: 442 ms
```
