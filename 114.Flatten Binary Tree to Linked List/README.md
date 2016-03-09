第一版因为看到顺序为先序遍历。

所以就想到从最后一个开始，这样就不会影响遍历。

这样顺序就由中-左-右变为右-左-中。

值得注意的除了把cur.right赋值为pre，还得把cur.left赋值为None。

```
225 / 225 test cases passed.
Status: Accepted
Runtime: 57 ms
```
