第一版就是分别用二分法找出存在重复元素的左边和右边的下标。

然后判断是否与target相等(容易忽略)即可。

时间复杂度为O(log(n))。

submit的结果为:
```
81 / 81 test cases passed.
Status: Accepted
Runtime: 48 ms
```

第二版也是利用二分法，但利用了target-0.5，和target+0.5来调用同一函数。

值得注意的是lo, hi中的hi取值为len(nums)，这样才有可能会有返回len(nums)的情况。

时间复杂度为O(log(n))。

submit的结果为:
```
81 / 81 test cases passed.
Status: Accepted
Runtime: 48 ms
```
