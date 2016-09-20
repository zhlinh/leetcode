就是26进制的转换。

需要注意的是10进制是0-9，然后以10取余数。

而此处的26进制并不是0-25，而是1-26，所以需要每次在循环内部减1然后取余数。

submit的结果为:
```
18 / 18 test cases passed.
Status: Accepted
Runtime: 44 ms
```
