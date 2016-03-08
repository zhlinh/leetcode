第一版用了递归的方法。而且还是双重递归。

这。。。好吧。

一个递归用于求高度，一个递归用于求子树是否符合条件。

时间复杂度为O(n^2)

subimt的结果为:
```
226 / 226 test cases passed.
Status: Accepted
Runtime: 104 ms
```

第二版也是算高度，但仅用了一个递归。

因为从底部开始发现不符合条件后赋值高度为-1，然后在上一层中会检查是否为-1。

即不满足则迅速往上层返回，退出递归栈。

即这个会bottom-up的，第一版是top-down的，而top-down会有很多重复计算。

时间复杂度为O(n)。

subimt的结果为:
```
226 / 226 test cases passed.
Status: Accepted
Runtime: 84 ms
```
