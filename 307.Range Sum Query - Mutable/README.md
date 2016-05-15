用到了Segment Tree分段数，又称为Binary Indexed Trees。

比一般的树节点多了两个变量，start和end，然后用val来记录数组从start到end的和。

而且本节点的值等于左子树的值加上右子树的值。

左子树保存的是从start到mid的值，而右子树保存的是从mid+1到end的值。

其中mid = start + (end - start) // 2。

这样更新一个叶子节点的值，只需更新从根节点到叶子节点经过的节点即可，复杂度为O(log(n))。

而计算从某个i到某个j(i<=j)的和所需要的时间也是O(log(n))。

计算和的时候如果是j<=mid，就进入到左子树中计算。
如果是i>mid，就进入到右子树中计算。
横跨两个子树的情况就到左子树中计算i到mid，到右子树中计算mid+1到j的值，返回两个的和。

submit的结果为:
```
10 / 10 test cases passed.
Status: Accepted
Runtime: 628 ms
```
