第一版的思路是记录第一个为负数的位置start，并计算出现负数的个数。

如遇到0则重新开始记录，dp也重新开始。

dp只负责记录连乘的值。

然后如果负数个数为奇数，则比较当前res和当前dp除以dp[start]的大小。

时间复杂度为O(n)。

submit的结果为:
```
183 / 183 test cases passed.
Status: Accepted
Runtime: 72 ms
```

第二版用了一个pMax和一个nMax记录当前的正数最大值和负数最大值。

当然pMax也有为0的时候，所以要注意如果nums的长度为1时直接返回nums[0]。

遇到负数，pMax和nMax交换，乘法规律就不用多说了。

遇到0，pMax和nMax都会变为0，相当于重新开始。

这样就相当于pMax把一个连乘为正数的组合都遍历了。

再用一个res比较当前res和pMax即可。

submit的结果为:
```
183 / 183 test cases passed.
Status: Accepted
Runtime: 56 ms
```
