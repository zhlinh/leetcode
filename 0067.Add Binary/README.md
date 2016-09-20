第一版用了传统的加法思路。

时间复杂度为O(n)。

submit的结果为:
```
294 / 294 test cases passed.
Status: Accepted
Runtime: 69 ms
```

第二版将carry移至循环条件，可以精简代码。

另外加了一些a或b为空时的判断，可以避免不必要的执行操作。

submit的结果为:
```
294 / 294 test cases passed.
Status: Accepted
Runtime: 56 ms
```
