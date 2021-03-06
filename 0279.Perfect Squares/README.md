用的DP的思想。

就是一个数可以表示成某个数加上j*j。

这样就是dp[i] = min(dp[i], dp[i-j*j] + 1)。

dp[i]表示平方数的个数。

之所以用到静态变量，是因为多次调用时可以用之前的结果。

即只要是小于当前dp长度的，直接返回dp[n]即可。

否则逐一往下计算dp值。

初始化dp = [0]。

时间复杂度为O(n^2)。

submit的结果为:
```
600 / 600 test cases passed.
Status: Accepted
Runtime: 332 ms
```

第二版是数学的方法，真的是在数学面前其他都是浮云啊。

首先任何一个数都可以表示成4个以内的数的平方和，所以答案只有1, 2, 3, 4。

然后先判断是否为1，即是否为平方数。

接着判断是否符合(4^a)*(8b+7)的形式。如果是则返回4。

上述判断过程需要逐步除以4，直到结果不为4的倍数为止，就可以判断n % 8 == 7。
可以保留改变n的值，因为不影响之后是否为2的判断。

最后判断是否为2，就是用n - i * i是否为平方数来判断，i从1到int(math.sqrt(n))。

为什么之前除以4的倍数不影响，
因为(4^a) * (b^2 + c^2) = 2^(2a) * (b^2 + c^2)
                        = (b * 2^a)^2 + (c * 2^a)^2
所以除以4的倍数不影响判断是否为2个数的平方和。

submit的结果为:
```
600 / 600 test cases passed.
Status: Accepted
Runtime: 56 ms
```
