一开始想着就遍历整个list两两相加的结果与target作比较，时间复杂度为O(n^2)。

submit的结果为:
```
16 / 16 test cases passed.
Status: Accepted
Runtime: 5924 ms
```

后来看了其他人的答案，用到了hash表的dict，键值对为数值->位置，然后检索dict中
key是否存在(target-数值)即可。时间复杂度为O(n)。

submit的结果为:
```
16 / 16 test cases passed.
Status: Accepted
Runtime: 52 ms
```
