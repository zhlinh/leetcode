第一版用了中序遍历，判断当前值大于上一个值。

err数组的长度有可能是2也有可能是4，但都是交换第一个和最后一个元素。

当然用两个变量即可，先找到第一个(first==None)时，然后第二个再变化(first!=None)。

用递归解决遍历的事也可以。关键就是改动中间需要做的事的部分。

submit的结果为:
```
74 / 74 test cases passed.
Status: Accepted
Runtime: 76 ms
```
