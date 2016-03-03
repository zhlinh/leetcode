第一版试错了好多次。

需要考虑的情况：

先排除”0”, “00”, “30”

遇到“0”, count -= 2，因为最后一个1或2相当于没了，然后按边界考虑。

考虑已到达边界以及27, 28, 29的伪边界的情况，count -= 1。

submit的结果为:
```
259 / 259 test cases passed.
Status: Accepted
Runtime: 52 ms
```
