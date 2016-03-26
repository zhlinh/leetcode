这个主要是需要再考虑第一个元素和最后一个元素相邻的情况。

所以就把这个分为求去掉第一个元素时所得的最大值和去掉最后一个元素时多得的最大值。

因为第一个元素和最后一个元素不能同时出现。

然后这两者取最大值就是所求了。

值得注意的是需要另外考虑数组长度为1的时候的情况，直接返回该元素，否则会把该元素去除的。

submit的结果为:
```
74 / 74 test cases passed.
Status: Accepted
Runtime: 48 ms
```

将第一版的分为奇偶改为了include和exclude两个。

意思是是否包含当前点，包含的只需要更新exclude + num[i]即可。

exclude需要取max(exclude, 上一次的include(需要先tmp存起来))。

这样表示取不包含当前点且是否包含前一点的最大值。

submit的结果为:
```
74 / 74 test cases passed.
Status: Accepted
Runtime: 48 ms
```
