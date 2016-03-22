第一版用了dic。

submit的结果为:
```
42 / 42 test cases passed.
Status: Accepted
Runtime: 76 ms
```

第二版一开始想到的是用排序，然后觉得时间复杂度可能会更高，所以就没用。

然后看了别人的答案，学到了一个Moore Majority Voting Algorithm(摩尔多数投票算法)。

先选定第一个作为major。

之后出现与之不同的数票数减1，相同则票数加1，票数为0重新选择major。

这样最后剩下的major至少会有1票。

submit的结果为:
```
42 / 42 test cases passed.
Status: Accepted
Runtime: 52 ms
```
