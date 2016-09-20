第一版用的DFS，先由大到小排序。

然后按当前值能乘以的最大倍数往下递减，并进入下一层。

原先以为只要amount减到0就可以迅速收敛退出dfs。

可是这样得到的并不是次数最小的。

举个例子:

如coins = [186,419,83,408], amount = 6249

第一次减到0的时候为`8*419`, `4*408`, `1*186`, `13*83`，次数的总和为26。

而正确答案应该是`5*419`, `8*408`, `4*186`, `3*63`，次数的总和为20。

所以得到一个结果后，只能用当前值与历史结果对比进行剪枝。

只有当count + 1 < self.times的时候才进入下一层。

self.times初始化为int的最大值。

当然这在[1], int的最大值的时候可能会有问题，因为会被判断为无解而返回-1。

所以可以将self.times初始化为long的最大值，最后再转为int。

时间复杂度为O(n^2)。

还有一种是用DP的方法，但是时间复杂度达到了O(n*amount)，而amount有可能是很大的数，
所以会特别慢。

DP主要的思路是这样:
```
dp = [amount+1] * (amount + 1)
dp[0] = 0
for coin in coins:
    for i in range(coin, amount + 1):
        dp[i] = min(dp[i], dp[i-coin] + 1)
return -1 if dp[amount] == amount + 1 else dp[amount]
```

就是把由coins得到的每一种排列组合i都放到dp[i]中，计算其最小值。
如果能排列到amount则返回其值否则返回-1。

这个会比DFS慢很多。不过这种计算每种排列的DP的思想值得借鉴，用二重循环计算一维DP。

submit的结果为:
```
180 / 180 test cases passed.
Status: Accepted
Runtime: 280 ms
```
