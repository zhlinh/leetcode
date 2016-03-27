第一版实现了一个快速排序，然后时间复杂度为O(nlog(n))。

submit的结果为:
```
31 / 31 test cases passed.
Status: Accepted
Runtime: 3216 ms
```

引入随机的pivot，而不总是第一个数之后，速度真的大大提升啊。

虽然最坏情况O(nlog(n))没有变。

但平均的时间复杂度为O(n)。

submit的结果为:
```
31 / 31 test cases passed.
Status: Accepted
Runtime: 64 ms
```
