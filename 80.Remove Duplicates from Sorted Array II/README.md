第一版用了dic来统计数字出现的次数。

submit的结果为:
```
164 / 164 test cases passed.
Status: Accepted
Runtime: 72 ms
```

第二版用了更简便的方法，因为nums是已排序的。

故只要nums[i] > nums[res-2]，则可满足条件。

submit的结果为:
```
164 / 164 test cases passed.
Status: Accepted
Runtime: 72 ms
```
