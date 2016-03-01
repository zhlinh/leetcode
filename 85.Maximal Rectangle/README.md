一开始想到的也是DP，想用一个二维的DP，但是实在分析不出来如何递进。

然后看了别人的答案，发现需要用三个一维的DP，left, right, height维护本行的值。

思路相当赞。用行来作为大循环。

left和right都可由前一个和当前值的比较得出。

hight由当前值得出是否需要与前一个的值相加。。

submit的结果为:
```
65 / 65 test cases passed.
Status: Accepted
Runtime: 160 ms
```

第二版用的是上一题Largest Rectangle in Histogram的思路。

只需要维护本行的一个height。

值得注意的是height的长度为n + 1，最后一个元素为0。

另外stack在每次新的一行时需要清空。

submit的结果为:
```
65 / 65 test cases passed.
Status: Accepted
Runtime: 156 ms
```
