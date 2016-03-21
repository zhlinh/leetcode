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
