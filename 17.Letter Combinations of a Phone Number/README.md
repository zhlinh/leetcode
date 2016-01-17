考虑清楚数学关系就好了，将数字对应的每个字母依次重复地添加到字符串数组中。

提交了一版，时间复杂度为O(n^2)。

submit的结果为:
```
25 / 25 test cases passed.
Status: Accepted
Runtime: 44 ms
```

第二版免去了数学运算，时间复杂度为O(n^2)。

虽比第一版要慢，但更易于理解。

新来一个非0或1的数字，就在原有的rList上分别添加所对应的字母。

把rList长度扩充3或4倍。

submit的结果为:
```
25 / 25 test cases passed.
Status: Accepted
Runtime: 52 ms
```