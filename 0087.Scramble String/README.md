一开始还以为分割是从中间len(s1//2)分的，提交时发现是随意分割的。

这就相当于用递归来穷举了，然后直接LTE了。

然后看了别人的答案，发现可以用一个dict来计算字母出现的次数，用来避免LTE。

但效率依旧很低。

submit的结果为:
```
281 / 281 test cases passed.
Status: Accepted
Runtime: 100 ms
```

第二版也是递归，不过用的是sorted以及增加了判断m < 4。

因m < 4时可任意排列。

另外精简了下代码。

submit的结果为:
```
281 / 281 test cases passed.
Status: Accepted
Runtime: 80 ms
```
