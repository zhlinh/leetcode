第一版因为看到顺序为先序遍历。

所以就想到从最后一个开始，这样就不会影响遍历。

这样顺序就由中-左-右变为右-左-中。

值得注意的除了把cur.right赋值为pre，还得把cur.left赋值为None。

```
225 / 225 test cases passed.
Status: Accepted
Runtime: 57 ms
```

第二版用的递归，和第一版的思路一样，也是右-中-左。

值得注意的是需要在每次进入口函数的时候赋pre为None，因类变量或实例变量会有记忆。

当然你也可以每解一次就新建一个类。


```
225 / 225 test cases passed.
Status: Accepted
Runtime: 52 ms
```
