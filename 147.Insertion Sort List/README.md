这也是一种很赞的解法。

哈哈，其实是另外开辟了一个链表。但依然是O(1)的空间，只是断开了而已。

一般会将dummy和head连起来。

而这里把它们断开，这样就避免了需要插入在最末即cur不用动的特殊处理。

另一个小技巧是不用每次都将iter移到dummy从头检查。否则会LTE，特别是已排序的链表。

只有在cur.val小于当前iter.next.val时时才需要从头检查。

否则就在当前位置开始检查即可。

submit的结果为:
```
21 / 21 test cases passed.
Status: Accepted
Runtime: 272 ms
```

