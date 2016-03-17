用了DP的方法，一开始想到的是用DFS，然后就被LTE了。。。

判断dp用的是以s的当前位置往前寻找另一个dp为真的位置。

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
