一开始的思路是用一个数作为target，然后找另外的两个数使三数相加为0。

这样就和第一题求Two Sum类似了。

只需解决排序和避免重复的问题。

提交了一版，时间复杂度为O(n^2)。

submit的结果为:
```
311 / 311 test cases passed.
Status: Accepted
Runtime: 792 ms
```

看到别人更好的解决思路。

先将数组排序，然后再从两边向中间搜索。避免重复只需三个判断即可。

对于已排序的序列，这种两边往中间靠拢的方法一定要get起来。

时间复杂度为O(n^2)。

submit的结果为:
```
311 / 311 test cases passed.
Status: Accepted
Runtime: 204 ms
```
