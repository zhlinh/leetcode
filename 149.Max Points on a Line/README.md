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

第二版优化了一下key的问题，这次用(x1-x0, y1-y0)的tuple作为key。

用的公式是(y-y0) = k(x-x0)，其中k=(y1-y0)/(x1-x0), 当x1-x0不等于0时。

当然tuple中的两个差值是约过的，即除以了最大公约数。

这样才能保证相同斜率的会在一个key里。

这样可以有效避免浮点数的精度所带来的问题。

这样另外一个需要关心的就是横截量。

所以这版会在每一个大循环之后清空一次dict，即只保留确定y0, x0和斜率的dict。

这样也就解决了问题。

需要注意的是重复点用一个overlap确定，之后需要在大循环里加overlap再加1。

即加上点(x0, y0)的个数。然后再取一次最大值。

这样是为了考虑都是重复点的情况。

submit的结果为:
```
27 / 27 test cases passed.
Status: Accepted
Runtime: 88 ms
```
