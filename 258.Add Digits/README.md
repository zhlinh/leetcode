数学题，好吧，具体资料可以看[Digital root - wiki](https://en.wikipedia.org/wiki/Digital_root)

简单的解释一下原理。

N = (a[0]*1 + a[1]*10 + ... +a[n]*10^n), and a[0]...a[n] are all between [0,9]

we set M = a[0] + a[1] + ... + a[n], 即为题目所求

and another truth is that:

1 % 9 = 1

10 % 9 = 1

100 % 9 = 1

so N % 9 = a[0] + a[1] + ... + a[n]

当然第一遍的a[0] + a[1] + ... + a[n]可能大于9，但N % 9 可以看做循环到小于等于9为止。

means N % 9 = M

as 9 % 9 = 0,so we can make (N - 1) % 9 + 1 to help us
solve the problem when N is 9.as N is 9, ( 9 - 1) % 9 + 1 = 9

设置成(N - 1) % 9 + 1是为了让N = 9的时候结果也是9，而不是0。

另外需要注意的是N = 0的时候，因为 N - 1会等于-1，在python中需要另外考虑，否则会出错。

所以当N = 0时直接返回0。

submit的结果为:
```
1101 / 1101 test cases passed.
Status: Accepted
Runtime: 68 ms
```
