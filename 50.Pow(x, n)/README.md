第一版用了递归的方法，double的是x，思想是pow(x, n) == pow(x*x, n-1)。

当然还可以利用pow(x, n) = pow(x/2, n) * pow(x/2, n)，double的是pow。

值得注意的是n为负数时候的处理，然后取反为正值时注意int的范围可能会overflow。

此处利用的是返回1.0 / (x * pow(x, -(n+1)))，这是比较好的解决办法。

submit的结果为:
```
20 / 20 test cases passed.
Status: Accepted
Runtime: 44 ms
```
