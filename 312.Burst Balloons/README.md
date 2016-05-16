只想到了O(n!)的方法。唉。。。

想到就分治的方法，将本来的数组首尾添上1，然后目的就是逐步删除首尾中的所有数。

在删除1个数的时候分为左半部份，删除的自身，右半部份。

即
```
dp[left][right] = max(dp[left][right], dp[left][i] + balloons[left] * i * balloons[right] + dp[i][right])
```

当然因为是由上至下的分支，其中dp[left][i]，dp[i][right]需要用类似helper()的递归完成。
直到left + 1 等于right的时候返回，即left和right中间没有数的时候，
也就是上一层的left + 2等于right的时候，删除i只有一个选择。

至上而上可以用一个cache来优化，也是常用的优化手段，此处的dp数组就相当于cache。

然而，很明显地有另外一种自下而上的方法，这个才是真正的DP。

先由长度进行一个循环，先计算所有right减left的长度k为2的，然后逐步计算到长度为n-1的。

然后就是再用两个循环来计算dp。其中left从0到n-k-1，right等于left+k，而i从left+1到right-1。

i就是所要删除的数。dp的计算就可以直接用上述的式子完成。

dp本来是二维数组，但需要先控制长度，所以用了三重循环。

时间复杂度为(O(n^3))。

submit的结果为:
```
70 / 70 test cases passed.
Status: Accepted
Runtime: 504 ms
```
