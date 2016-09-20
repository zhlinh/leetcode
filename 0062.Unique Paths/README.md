第一版一开始还用DFS写了一个求全部的排列组合的，然后超时了。

然后就想到直接用数学知识求解个数了。

    Combination(N, k) = n! / (k!(n - k)!)

时间复杂度为O(N)。N = k + n - k

submit的结果为:
```
61 / 61 test cases passed.
Status: Accepted
Runtime: 40 ms
```

第二版就是把公式化简下，得到时间复杂度更小的解法。

Combination(N, k) = ( (n - k + 1) * (n - k + 2) * ... * (n - k + k) ) / k!

时间复杂度为O(k)。

submit的结果为:
```
61 / 61 test cases passed.
Status: Accepted
Runtime: 40 ms
```

第三版用了DP，虽然会更慢，但也是挺有意思的解法，核心思想为:

    dp[i][j] = dp[i-1][j] + dp[i][j-1]

即到当前位置的解法数为前一步的解法数之和。i或j为0时dp[i][j] = 1

时间复杂度为O(n * m)。

submit的结果为:
```
61 / 61 test cases passed.
Status: Accepted
Runtime: 48 ms
```
