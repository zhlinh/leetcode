用了二分法，重要的是需要知道nums[mid]需要与谁比较。

此处需要找出的是当前元素比后面的元素大的所在位置。

利用该特点也可以用线性方法来解，只要nums[i] < nums[i-1]，则返回i-1。

当然二分法的时间复杂度为O(log(n))。

submit的结果为:
```
58 / 58 test cases passed.
Status: Accepted
Runtime: 48 ms
```
