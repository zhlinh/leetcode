第一版用了传统的加法思路，这样的话加n都没问题。

时间复杂度为O(n)。

submit的结果为:
```
108 / 108 test cases passed.
Status: Accepted
Runtime: 44 ms
```

第二版就根据加1的特点，小于9时，直接+1返回值。

只有等于9时才会进位继续循环，进位后该位0。

这样就精简了代码。

时间复杂度为O(n)。

submit的结果为:
```
108 / 108 test cases passed.
Status: Accepted
Runtime: 44 ms
```
