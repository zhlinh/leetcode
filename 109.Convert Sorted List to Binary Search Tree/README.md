第一版用了递归的方法。每次都要找中间节点。然后中间节点的前一个pre.next赋值None。

找中间节点是通过一个slow=slow.next和一个fast=fast.next.next来找的。

找中间节点的思路挺不错的。

subimt的结果为:
```
32 / 32 test cases passed.
Status: Accepted
Runtime: 308 ms
```

第二版也是递归，不过是先计算出ListNode的长度。

然后用的中序遍历，以n为参数，把树给建起来。相当赞的思路。

值得注意的是参数的传递，传递一直需要变化而不需要回溯的参数时，用了一个数组。

subimt的结果为:
```
32 / 32 test cases passed.
Status: Accepted
Runtime: 268 ms
```
