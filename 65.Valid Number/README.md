这道题折腾了好久，因为不知道怎样才算作有效的数字。

第一版先将s去掉首尾的空格，然后在一个循环里判断。

需添加的flag有numberSeen, dotSeen, eSeen, numberAfterE。

感觉给的例子还不够完整，然后不断地试错。其正则表达式应为：

    [-+]?([0-9]+(.[0-9]*)?|.[0-9]+)(e[-+]?[0-9]+)?

时间复杂度为O(n)。

submit的结果为:
```
1481 / 1481 test cases passed.
Status: Accepted
Runtime: 96 ms
```

第二版即将正则表达式实现，?的用if，+的用n来记录个数并保证其大于0，*的用while。

最后判断i == len(s)。

时间复杂度为O(n)。

submit的结果为:
```
1481 / 1481 test cases passed.
Status: Accepted
Runtime: 80 ms
```
