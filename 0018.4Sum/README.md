先提交了一版，时间复杂度为O(n^3)。

submit的结果为:
```
282 / 282 test cases passed.
Status: Accepted
Runtime: 1364 ms
```

第二版加了些判断条件，充分利用已排序的性质，及时跳出不可能的情况。

时间复杂度为O(n^3)，但效率已经有了质的飞跃。

submit的结果为:
```
282 / 282 test cases passed.
Status: Accepted
Runtime: 128 ms
```

第三版用了递归，写了个比较通用的，可以计算N-Sum(N>=2)的。

时间复杂度为O(n^3)。

submit的结果为:
```
282 / 282 test cases passed.
Status: Accepted
Runtime: 128 ms
```
