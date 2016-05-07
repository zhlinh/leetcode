第一版用了三个数组，分别存放当前ugly乘2或乘3或乘5的数。

然后下一个的ugly取三个数组中的最小值。

然后需要注意的是有可能三个数组中会有重复的，即可能同时出现最小值。

此时需要同时移动下标或同时pop掉第一个数。

submit的结果为:
```
596 / 596 test cases passed.
Status: Accepted
Runtime: 252 ms
```
