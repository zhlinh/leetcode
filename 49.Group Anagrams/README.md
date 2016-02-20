第一版用了dic，sorted(s)作为key，然后s作为value逐一添加。

需另外考虑的是对于s为””(空字符串)时的处理，因为空字符串无法作为dic的key。

submit的结果为:
```
20 / 20 test cases passed.
Status: Accepted
Runtime: 252 ms
```
