其实就是找出从左往右第一个小于等于最后一个数的点。

然后就是二分法了。

对于有重复元素，关键在于去除类似[3, 1, 3]这种情况，即首尾相同的情况。

若按原先解法则会得到3，因为这也是小于等于最后一个数的点。

所以得把最后一个数给往前移，即找出不等于第一个数的点作为最后一个数。

去除的数不会影响结果，因为是重复元素。

这样也就使原先的解法生效了。

submit的结果为:
```
188 / 188 test cases passed.
Status: Accepted
Runtime: 48 ms
```

第二种解法的思路是从左往右找小于本次二分法的的终点的点。

即比较的值会一直在变化，这样也可以有效地缩小范围。

需要注意的是当nums[mid] == nums[j]时，j -= 1。即出现相同元素的处理。

submit的结果为:
```
188 / 188 test cases passed.
Status: Accepted
Runtime: 48 ms
```