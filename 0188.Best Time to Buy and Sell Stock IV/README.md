就是维护一个hold数组和一个release数组，其长度为可交易的数目。

需要注意的是如果可交易的数目大于prices的长度的一半，则转为贪心算法。

即如果当前与前一天的差值大于0的则累加到res中。这样可避免memory error。

submit的结果为:
```
211 / 211 test cases passed.
Status: Accepted
Runtime: 124 ms
```
