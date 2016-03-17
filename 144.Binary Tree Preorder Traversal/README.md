第一版用了中序的底子，但是另外加了一个visited的set避免重复。

这样就可以在每次有左子树或右子树的时候就添加进res。

submit的结果为:
```
67 / 67 test cases passed.
Status: Accepted
Runtime: 48 ms
```

第二版才是真正的先序遍历，pop，然后先压入right，再压入left。

这个简直就是递归的堆栈模拟，哈哈。

当然此处判断了right或left是否为空再压入堆栈。

若不判断直接压入，然后在pop的时候判断，这就是和递归的堆栈完全一致了。

还有一种思路是只压入右子树，这样就可以往上跳到未遍历的右子树中。

submit的结果为:
```
67 / 67 test cases passed.
Status: Accepted
Runtime: 48 ms
```
