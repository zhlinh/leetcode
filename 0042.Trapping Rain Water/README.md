提交了第一版。先找出最高的所在位置。

然后从两边各一个循环逼近，值得注意的是增加water后需要移动直方的位置。

时间复杂度为O(n)。

submit的结果为:
```
315 / 315 test cases passed.
Status: Accepted
Runtime: 60 ms
```

第二版是从两边向中间逼近的思路，维护一个当前最小高度。

即当前最小高度减下一个位置的高度，当中的水都会有效，因左和右会有更高的作为保证。

时间复杂度为O(n)。

submit的结果为:
```
315 / 315 test cases passed.
Status: Accepted
Runtime: 60 ms
```
