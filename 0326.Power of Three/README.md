数学题，不过求最大的pow的方法可以借鉴一下。

```
maxPow3 = math.pow(3, math.log(0x7fffffff) // math.log(3)) % n == 0
```

然后就是

```
return n > 0 and maxPow3 % n == 0
```

即只要int中最大的3的pow值是n的倍数，且n大于0，则n是3的pow。

其实也就是最大的3的pow值的因数包含了所有3的pow值。

submit的结果为:
```
21038 / 21038 test cases passed.
Status: Accepted
Runtime: 476 ms
```
