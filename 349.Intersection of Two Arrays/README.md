求两个数组的公共元素，且要求没有重复元素。

很容易想到用set，然后实现就很简单了。时间复杂度为O(n)。

另外可以用排序，先将两个排序，然后用两个index，相同的话就加入，然后跳过重复元素。

还有就是二分法查找。

sumbmit的结果为:
```
60 / 60 test cases passed.
Status: Accepted
Runtime: 50 ms
```
