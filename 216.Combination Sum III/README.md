第一版就是一般的DFS。

submit的结果为:
```
18 / 18 test cases passed.
Status: Accepted
Runtime: 50 ms
```

第二版是N sums的思路，本质也是DFS。

只是寻找到最后两个的时候，利用了已排好序的性质，能更迅速地找到所求。

submit的结果为:
```
18 / 18 test cases passed.
Status: Accepted
Runtime: 44 ms
```
