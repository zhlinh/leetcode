第一版就按照最大长度加前面几行，然后再添加最后一行。

时间复杂度为O(n^2)。

submit的结果为:
```
24 / 24 test cases passed.
Status: Accepted
Runtime: 52 ms
```

第二版用了一个List来存储到前一个为止的string，即先判断后添加。

时间复杂度为O(n^2)。

submit的结果为:
```
24 / 24 test cases passed.
Status: Accepted
Runtime: 48 ms
```
