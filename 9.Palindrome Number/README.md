确实是道简单题，如果无空间要求，完全可以用一行代码写成。

return str(x) == str(x)[::-1]

要求不额外增加空间。

用纯数学的方法，提交了一版。需要注意的是负数都不是回文数。

submit的结果为:
```
11506 / 11506 test cases passed.
Status: Accepted
Runtime: 284 ms
```
