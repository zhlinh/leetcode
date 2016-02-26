最先想到的就是二分查找。

时间复杂度为O(log(n))。

submit的结果为:
```
1017 / 1017 test cases passed.
Status: Accepted
Runtime: 64 ms
```

第二版用了Newton Method(牛顿法)来解决。

解x^2 - n = 0，则有

x[k+1] = (1/2) * (x[k] + n/x[k])

submit的结果为:
```
1017 / 1017 test cases passed.
Status: Accepted
Runtime: 68 ms
```
