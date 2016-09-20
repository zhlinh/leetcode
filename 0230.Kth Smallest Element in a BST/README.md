用了中序遍历，即根据二叉搜索树的特点，`左 < 中 < 右`得到第k个最小值。

时间复杂度为O(k)。

submit的结果为:
```
91 / 91 test cases passed.
Status: Accepted
Runtime: 87 ms
```

第二版的思路是计算左子树的节点数目，与k进行比较，
然后定位所求是在左子树还是右子树中。

有点二分法的意味。

但是计算count就需要花费O(n)的时间。如果可以改变树的节点结构，
可以把这个作为变量添加进去。在初始化或增减的时候计算即可。

所以总的时间复杂度会为O(nlog(n))。

submit的结果为:
```
91 / 91 test cases passed.
Status: Accepted
Runtime: 88 ms
```
