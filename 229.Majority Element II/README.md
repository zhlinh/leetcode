用到的是Boyer-Moore Majority Vote algorithm多数票算法。

值得注意的是if的顺序，先判断是否有相等的，再判断是否count为0。

否则两个candidate会有可能相同，所以应该先搂住相等的，然后是count为0的，最后是不相等的情况。

submit的结果为:
```
66 / 66 test cases passed.
Status: Accepted
Runtime: 64 ms
```
