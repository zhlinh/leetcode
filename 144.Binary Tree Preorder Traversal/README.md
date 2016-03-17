第一版用了中序的底子，但是另外加了一个visited的set避免重复。

这样就可以在每次有左子树或右子树的时候就添加进res。

submit的结果为:
```
67 / 67 test cases passed.
Status: Accepted
Runtime: 48 ms
```
