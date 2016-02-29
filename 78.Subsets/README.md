第一版用了DFS。

submit的结果为:
```
26 / 26 test cases passed.
Status: Accepted
Runtime: 52 ms
```

第二版只用了循环。

例如nums=[1, 2, 3]。思路是这样的：

init: [[]]
add 1: [[], [1]];
add 2: [[], [1], [2], [1, 2]];
add 3: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]].

submit的结果为:
```
26 / 26 test cases passed.
Status: Accepted
Runtime: 60 ms
```
