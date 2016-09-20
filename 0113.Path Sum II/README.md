第一版用了DFS。

值得注意的是判定是否符合时需要无叶子节点时再判定。

若符合则将path加入数组中。

即root.left == None and root.right == None。

```
114 / 114 test cases passed.
Status: Accepted
Runtime: 88 ms
```
