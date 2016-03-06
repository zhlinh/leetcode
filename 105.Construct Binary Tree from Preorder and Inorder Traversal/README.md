第一版用了递归解法。

可以看先序的第一个即为root，然后找到中序所在的位置，其左右各为左子树和右子树。

先序的root的下一个个即为左子树的root。

然后由中序确定当前左子树的个数，在先序中往后移找到右子树的root。

依次递归，将所有的root确定。无子节点时返回None。

subimt的结果为:
```
202 / 202 test cases passed.
Status: Accepted
Runtime: 432 ms
```
