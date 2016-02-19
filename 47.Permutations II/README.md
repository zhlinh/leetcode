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
