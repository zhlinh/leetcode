第一版用了递归的方法。每次都要找中间节点。然后中间节点的前一个pre.next赋值None。

找中间节点是通过一个slow=slow.next和一个fast=fast.next.next来找的。

找中间节点的思路挺不错的。

subimt的结果为:
```
32 / 32 test cases passed.
Status: Accepted
Runtime: 308 ms
```
