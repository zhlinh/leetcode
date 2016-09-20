就是只有当p和q的值分别处于当前节点的两端或有一个与当前节点的值相等时返回当前节点。

如果都小于当前节点的值则检查左子树。

如果都大于当前节点的值则检查右子树

这次用了递归，当然也可以用循环来写。

```
while(True):
    # The first line is so fancy!
    if((p.val - root.val) * (q.val - root.val) <= 0):
        return root
    if(p.val < root.val):
        root = root.left
    else:
        root = root.right;
```

submit的结果为:
```
27 / 27 test cases passed.
Status: Accepted
Runtime: 128 ms
```
