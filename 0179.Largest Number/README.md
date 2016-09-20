本来想用Radix排序来做，但后来发现不行。

因为需要x+y和y+x相比较才能确定两个字符串的位置。

所以就用了内置的排序，但python3的排序不支持cmp了。

所以还用了工具函数包functools里的cmp_to_key。

把cmp转为可比较的对象。

这样就可以传入自己的比较函数作为key了。

submit的结果为:
```
221 / 221 test cases passed.
Status: Accepted
Runtime: 80 ms
```
