思路就是用四个变量分别记录买入后和卖出后的剩余钱。

然后返回第二次卖出的值。

非常简单的思路但就是木有想到。。。囧

时间复杂度为O(n)。

submit的结果为:
```
198 / 198 test cases passed.
Status: Accepted
Runtime: 68 ms
```

第二版用了DP来解，就是按照交易次数为大循环，然后再算hold和realease。

release作为DP，当然可以用二维DP方便理解，这里只用了一维。

用一维后顺序就不可以颠倒了，得先求hold，再求release。

因为hold的值需要依赖上一层大循环(上一次交易)的release。

而realease都是在本层(本次交易)中作比较，因为得先卖才能买。

卖出得到的hold就属于本层(本次交易)了。

时间复杂度为O(n)。

submit的结果为:
```
198 / 198 test cases passed.
Status: Accepted
Runtime: 72 ms
```
