提交了第一版，时间复杂度为O(n)。

submit的结果为:
```
208 / 208 test cases passed.
Status: Accepted
Runtime: 72 ms
```

优化了第一版的逻辑。并不再生成新的ListNode而是重新连接原来的两个ListNode。

即会改变原来的输入。这样稍微会快一些。

时间复杂度为O(n)。

submit的结果为:
```
208 / 208 test cases passed.
Status: Accepted
Runtime: 60 ms
```

第三版用了递归，而且是非尾递归，所以长ListNode可能会有栈溢出现象。

时间复杂度为O(n)

```
208 / 208 test cases passed.
Status: Accepted
Runtime: 60 ms
```
