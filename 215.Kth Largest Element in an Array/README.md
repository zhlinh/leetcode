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

第三版用了最大堆，其规则是数组中第i个元素大于等于第2i+1和2i+2个元素。

2i+1和2i+2小于数组的长度。

所以每次都取最大堆的最大值即顶部元素。

然后将该值置于与数组的最末值交换，接着最大堆的长度减一。

再重新由刚置于顶部的值开始重新构造最大堆。

重复k次后，取刚被置换出去的值即为所求。

时间复杂度为O(nlog(n))。

submit的结果为:
```
31 / 31 test cases passed.
Status: Accepted
Runtime: 300 ms
```
