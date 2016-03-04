第一版用了递归。是DFS的思想但有根普通的DFS有所不同。

每一层都是一个新的trees、新的left，新的right。

tress只需要维护根节点，即有多少个根节点就有多少棵子树。

而左子树和右子树添加的都是一个节点，即某个子树的根节点。

left = ..., right = ...。返回的会是一个或多个子树的根节点。

以当前i值作为根节点，把left和right集合添加进来，形成不同的子树，添进trees中。

返回此trees，以此作为上一层的left或right。

submit的结果为:
```
9 / 9 test cases passed.
Status: Accepted
Runtime: 100 ms
```
