提交了第一版，有点BFS的意思，会把nums划分为几个层级。

如[2, 3, 1, 1, 4], 可划分为[ 2 || 3 1 || 1 4 ]。

当前层级最大可到达的范围作为下一层级的划分依据。

时间复杂度为O(n)。

submit的结果为:
```
91 / 91 test cases passed.
Status: Accepted
Runtime: 68 ms
```

第二版也是分层的思路，但是代码更清晰明了。

时间复杂度为O(n)。

submit的结果为:
```
91 / 91 test cases passed.
Status: Accepted
Runtime: 68 ms
```
