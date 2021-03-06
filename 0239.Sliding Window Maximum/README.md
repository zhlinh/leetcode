终于做出了难度为Hard的题，还是有点小激动的。

思路是用两个deque，一个q存储数值，一个qi存储所在的位置。

q中保留的会是一个递减的序列。

当有一个新的数即将添加进来的时候，会pop掉最左侧和最右侧比它要小的数。

因为只要新的数的存活时间比之前的数要长，所以就没必要保留比它小的数。

这样就维护了一个递减的序列。

qi的作用是当q最左侧的数因为window的关系需要移除时需要位置信息，
因为靠q的大小无法判断是否应该移除最左侧的数。

当i >= k - 1的时候，即windows第一次满的一刻，开始把q[0]添加进res中，
则刚好为res的长度。

时间复杂度为O(n)。

submit的结果为:
```
18 / 18 test cases passed.
Status: Accepted
Runtime: 240 ms
```

版本二主要作了两处优化。

1. 只保留了qi，因为其实q[0]可以从nums[qi[0]]中获得，不必要维护两个deque。

2. 只保留了pop掉最右侧比即将添加的数要小的数，这样就已经足够维护一个递减的序列了。

时间复杂度为O(n)。

submit的结果为:
```
18 / 18 test cases passed.
Status: Accepted
Runtime: 220 ms
```
