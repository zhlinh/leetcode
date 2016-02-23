第一版的思路是先插入Interval，然后从当前位置(当前位置为0时)或前一个位置开始merge。

时间复杂度为O(n)

submit的结果为:
```
151 / 151 test cases passed.
Status: Accepted
Runtime: 88 ms
```

第一版的思路分为left，重叠的部分，right。

然后用一个循环来计算上述部分即可。

时间复杂度为O(n)

submit的结果为:
```
151 / 151 test cases passed.
Status: Accepted
Runtime: 88 ms
```
