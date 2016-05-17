第一版就和primes只有2，3，5的ugly number方法一样的。

只需将其扩展成了一个primes数组。

时间复杂度为O(kn)。

submit的结果为:
```
83 / 83 test cases passed.
Status: Accepted
Runtime: 1200 ms
```

第二版用heapq最小堆来优化了一下，使寻找最小值可以用O(log(k))来实现。

需要注意heapq除了存val外还需存入index和prime信息。

否则如果还需要额外寻找最小值所对应的prime和所对应的index就可能会浪费很多时间。

时间复杂度为O(log(k)n)。

submit的结果为:
```
83 / 83 test cases passed.
Status: Accepted
Runtime: 596 ms
```
