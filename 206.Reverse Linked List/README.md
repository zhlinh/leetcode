第一版就是常规循环解法，逐一把head的后一个节点挪到最前面。最后返回dummy.next。

submit的结果为:
```
27 / 27 test cases passed.
Status: Accepted
Runtime: 52 ms
```

第二版用的递归的方法，传入pre和head两个参数。

用了底部递归，因为需要返回最后一个节点。

然后每一层都是返回该节点直到退出栈。

submit的结果为:
```
27 / 27 test cases passed.
Status: Accepted
Runtime: 56 ms
```
