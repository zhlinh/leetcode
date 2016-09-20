一开始用了二维的DP来解，时间复杂度为O(n^2)，然后就悲剧地超时了。

然后需要在最前面加上一个关于p除去*的长度和s的长度的判断才勉强通过。

submit的结果为:
```
1801 / 1801 test cases passed.
Status: Accepted
Runtime: 1100 ms
```

第二版用了save_si和save_pi来作回溯用，确定*所代表的字符的个数。

时间复杂度为O(n)，相当巧妙的方法。

submit的结果为:
```
1801 / 1801 test cases passed.
Status: Accepted
Runtime: 128 ms
```

