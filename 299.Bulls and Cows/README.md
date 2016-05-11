先用一个循环得出bull，并把secret的数字的个数作个统计。

然后再用一个循环找出guess中猜到的数字的个数，此结果包含cow和bull的总和。
用该结果减去bull就可以得出cow了。

当然还可以用两个数组分别统计secret和guess除了bull之外的的数字个数。
然后取两个数组的每个数字的最小值累加起来即为cow。

submit的结果为:
```
151 / 151 test cases passed.
Status: Accepted
Runtime: 100 ms
```
