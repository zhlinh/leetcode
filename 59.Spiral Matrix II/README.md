第一版就是利用dirs存储方向，step存储步数。核心如下：

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        step = [n, n]

时间复杂度为O(n)。

submit的结果为:
```
21 / 21 test cases passed.
Status: Accepted
Runtime: 48 ms
```
