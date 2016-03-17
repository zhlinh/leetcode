用了DP的方法，一开始想到的是用DFS，然后就被LTE了。。。

判断dp用的是以s的当前位置往之前寻找另一个dp为真的位置。

判断两个之间的子字符串是否在wordDict中。

需要注意的是如果dp判断为真，则立即break。

即当前位置的dp就确定了，再往下判定下一位置的dp。

时间复杂度为O(n^2)。

sumbmit的结果为:
```
34 / 34 test cases passed.
Status: Accepted
Runtime: 60 ms
```

第二版用的也是DP。

但判断dp是以s的当前位置往后查找wordDict中的word是否与s的子字符串相等。

值得注意的是此时就不可以break了，因为循环中的dp[i+n]大部分情况下都不是同一个dp。

时间复杂度为O(n*m)。

sumbmit的结果为:
```
34 / 34 test cases passed.
Status: Accepted
Runtime: 52 ms
```
