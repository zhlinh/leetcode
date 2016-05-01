用了一个stack。

一开始以为是四则运算，后来发现只有加减。

然后需要考虑的就只有括号的问题了。

用了一个stack来存储之前的res和sign。

另外将减的情况归到符号为负的情况下，这样可以统一用res += sign * num来进行计算。

注意括号当出现)才进行计算，出现(时存入stack。

submit的结果为:
```
37 / 37 test cases passed.
Status: Accepted
Runtime: 227 ms
```
