第一版就用了两个index和一个记录相同时数值的变量。

需要注意的是最后一个ListNode的处理。

submit的结果为:
```
166 / 166 test cases passed.
Status: Accepted
Runtime: 76 ms
```

第二版只用了两个index。思路相当好。

让p跑到与前面一个元素不相同的元素下，然后判断l.next是否等于p。

若相等，l = l.next。若不等，l.next = p.next。

submit的结果为:
```
166 / 166 test cases passed.
Status: Accepted
Runtime: 60 ms
```
