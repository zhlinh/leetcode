第一版用了BFS，就是不断地通过调换别的元素到当前位置来扩充叶子节点的规模。

而对于重复元素的考虑，即保证当前位置start的元素不能重复，用了一个dic来避免。

submit的结果为:
```
25 / 25 test cases passed.
Status: Accepted
Runtime: 120 ms
```

第二版用DFS，也是用了dic来避免当前位置的重复。

submit的结果为:
```
25 / 25 test cases passed.
Status: Accepted
Runtime: 116 ms
```

第三版也是DFS，但先排序，然后换交换位置后并不交换回来。

在此例的DFS递归中都不需要交换回来。(DFS一般需恢复原样)

因为都是一个个位置来确定的，到最后一层才完全确定序列。

与当前start位置之后的序列顺序并无关系。

这样简单地与上一次start位置的元素相比较就可替换不重复的元素。

submit的结果为:
```
25 / 25 test cases passed.
Status: Accepted
Runtime: 120 ms
```
