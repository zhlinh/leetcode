第一版就是先排序，然后按定义找。

从h的最大值n开始找起，n为citations数组的长度。

submit的结果为:
```
81 / 81 test cases passed.
Status: Accepted
Runtime: 48 ms
```

第二版用了另外一个数组count，数组长度为length + 1。

因为h的值范围在0到length，长度为length + 1。

count[0]到count[length-1]表示citation等于下标i的个数。

count[length]为citation大于等于length的个数。

然后由后往前一个循环count，累计计算个数加到total中。

total即为citation大于下标i的个数。

当找到total >= i 就返回i即为所求。

submit的结果为:
```
81 / 81 test cases passed.
Status: Accepted
Runtime: 48 ms
```
