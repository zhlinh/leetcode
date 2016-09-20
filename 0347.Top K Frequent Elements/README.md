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

其实一般是不考虑常数的，所以也只能是说稍微better than O(n(log(n)))。
因为如果n很大，一切都是浮云。

sumbmit的结果为:
```
20 / 20 test cases passed.
Status: Accepted
Runtime: 68 ms
```

第二版用了Bucket Sort的思想，这也是比较常用的方法。

以num出现的数量freqs作为数组，每个freqs[i]储存等于该频率i的num。

这样就可以由freqs从右往前逐一加入res，直到res的大小大于等于k。

然后返回截取前k个即为所求。

因为合并最后一个加入的频率所对应的num数组时可能会超过k。

当然不采用合并num数组的方式而是一个个添加num就不会产生超过k的问题。

另外一种实现是用freqs[i]储存等于该频率的num的个数。

然后从右往左k -= freqs[i]，直到k == 0，记下此时的下标i作为前k个的最小频率值last。

然后将大于等于该最小频率值last的num加入到res中。

如果要准确加入，此时的k减去频率的数量后小于等于0。
```
    if dic[key] > last || (dic[key] == last && k > 0):
        if dic[key] == last:
            k += 1
```
这样就保证了遇到等于last但属于多出来的就先跳过abs(k)个，然后就都加上。

很妙的方法。

sumbmit的结果为:
```
20 / 20 test cases passed.
Status: Accepted
Runtime: 80 ms
```
