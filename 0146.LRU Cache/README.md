了解LRU的原理之后剩下的就是数据结构的选择了。

选用了dict来选取已存在页面，当为get之时，不存在就返回-1。

当为set时，不存在就新建一个页面，然后将之置于最前，页面数满时则删除最末页面。

每次访问或修改某页面的时将该页面置于最前。

这也就是Least Recently Used的精髓。

页面的组织用了双向链表，首尾各一个虚索引，方便插入在最前或删除最末页面。

submit的结果为:
```
17 / 17 test cases passed.
Status: Accepted
Runtime: 220 ms
```

