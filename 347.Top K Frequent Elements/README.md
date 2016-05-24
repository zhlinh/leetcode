不排序的话很容易想到用heapq最小堆或叫优先队列来实现。

先用dic计算每个num的数量。

将num的数量作为heapq的值，num的数量和num绑定在一个tuple中就可以push了。

num的数量要取反，因为要将最小堆转为最大堆。

要想比O(n(log(n)))要小，关键在于控制heapq的大小。

将heapq的大小控制在n-k，则多出来后pop掉最顶上的肯定为前k个最大的。

这样时间复杂度就变为了O(n(log(n-k)))。

做到这很容易想到如果k很小是不是很浪费，所以优化的话可以判断k是否比n//2要大，

k>n//2的话就用上述方法。

k<=n//2的话就保持heapq为最小堆，且大小为k，pop掉的肯定为n-k个最小的。

如果作此改进则可以保证时间复杂度为O(n(log(n//2)))。

sumbmit的结果为:
```
20 / 20 test cases passed.
Status: Accepted
Runtime: 68 ms
```
