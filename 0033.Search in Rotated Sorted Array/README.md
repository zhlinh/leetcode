提交第一版，很容易想到二分法。

但因为是旋转的sorted list，需要另外判断是否符合升序排列。

submit的结果为:
```
194 / 194 test cases passed.
Status: Accepted
Runtime: 56 ms
```

第二版先找出旋转的起点，然后再用二分法来寻找。

submit的结果为:
```
194 / 194 test cases passed.
Status: Accepted
Runtime: 52 ms
```
