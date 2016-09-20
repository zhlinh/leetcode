第一次提交的版本用两重循环减除数的倍数。

时间复杂度为O(log(n)*log(n))。

submit的结果为:
```
988 / 988 test cases passed.
Status: Accepted
Runtime: 64 ms
```

第二版也是循环减去除数的倍数。

但这次先计算出最大的倍数，然后再往小的减。

故仅需一重循环。时间复杂度为O(log(n))。

submit的结果为:
```
988 / 988 test cases passed.
Status: Accepted
Runtime: 56 ms
```
