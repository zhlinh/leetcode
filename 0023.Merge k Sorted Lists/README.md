第一版是基于合并两个ListNode的，首尾两个逐渐往中间合并，加到新的List中。

新的List大约为原长度一半大小。

然后再按此方法循环，最终得到长度为1的时候，就是合并完成的ListNode。

时间复杂度为O(nlogk)。

submit的结果为：
```
130 / 130 test cases passed.
Status: Accepted
Runtime: 172 ms
```

第二版几乎是第一版的思路，只是改为递归来实现，这也是merge的常用方法。

时间复杂度为O(nlogk)。

submit的结果为：
```
130 / 130 test cases passed.
Status: Accepted
Runtime: 144 ms
```

第三使用了Python的Heapq，类似Java的PriorityQueue，即最小堆的实现。

父节点比子节点要小。

时间复杂度为O(nlogk)。

submit的结果为：
```
130 / 130 test cases passed.
Status: Accepted
Runtime: 112 ms
```
