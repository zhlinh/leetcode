第一版就是直接法，规律是除首尾外均由肩上元素相加而得。

还有一种思路是该层等于[0]+[上一层] + [上一层]+[0]。

即[1, 2, 1] = [0, 1, 1] + [1, 1, 0]。

但这样相加就得另外一个函数。不过如果是python的话用lambda也挺简洁的。

```
15 / 15 test cases passed.
Status: Accepted
Runtime: 48 ms
```
