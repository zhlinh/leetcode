第一版用了ax + by +c = 0的直线公式。

然后分横线，竖线和斜线三种情况[因为直接求斜率分母可能为0]。

求得a, b, c后以字符串形式的”a,b,c”作为key将下标i和j以set的形式存入dic中。

这样dic中的某个key所存的set的长度即为在同一直线上的点的数目。

submit的结果为:
```
27 / 27 test cases passed.
Status: Accepted
Runtime: 164 ms
```
