第一版用了中序遍历，判断当前值大于上一个值。

需要注意的是上一个值lastval的初始化。

一开始设为int的最小值，但会出现只有一个节点且该节点为int最小值的情况。

于是将用了一个标志，将中序遍历的第一个值赋给lastaval。

submit的结果为:
```
74 / 74 test cases passed.
Status: Accepted
Runtime: 76 ms
```

第二版用了一个pre记录上一个节点，可以让代码更简洁。

submit的结果为:
```
74 / 74 test cases passed.
Status: Accepted
Runtime: 68 ms
```
