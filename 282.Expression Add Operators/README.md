用了DFS。

需要注意的是遇到乘的时候的处理，因为运算顺序。
所以需要保留上一次相加相减或相乘的结果作为backup，
然后再乘的时候减去上次的结果backup，再加上这次backup * cur的结果。

然后还需要注意二位数及以上首位是0的情况的去除，如05,005等。

submit的结果为:
```
20 / 20 test cases passed.
Status: Accepted
Runtime: 1659 ms
```
