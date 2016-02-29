第一版先找出rotate的起点，然后再由此求出realmid，其他同标准的二分法。

submit的结果为:
```
271 / 271 test cases passed.
Status: Accepted
Runtime: 56 ms
```

第二版就是一般的rotate的解法，放在一个循环里，需另外比较mid和lo, hi对应值的大小。

另外因为多了重复元素的情况。

所以需要增加当mid, lo, hi对应元素都相等时: lo+=1, hi-=1。


submit的结果为:
```
271 / 271 test cases passed.
Status: Accepted
Runtime: 60 ms
```
