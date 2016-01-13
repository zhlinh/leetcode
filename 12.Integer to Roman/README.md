先介绍下罗马数字:

any of the letters representing numbers in the Roman numerical system:

I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1,000.

In this system a letter placed after another of greater value adds

(thus XVI or xvi is 16),

whereas a letter placed before another of greater value subtracts

(thus XC is 90).

然后只要个十百千位各建一个数组索引，便可以很容易转换了。

先提交了一版，还用到数组翻转之类，比较繁琐。

submit的结果为:
```
3999 / 3999 test cases passed.
Status: Accepted
Runtime: 116 ms
```

然后第二版改进了下，只用到了字符串相加。

submit的结果为:
```
3999 / 3999 test cases passed.
Status: Accepted
Runtime: 108 ms
```
