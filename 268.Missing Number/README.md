一开始还以为是排序好的，举的例子就不能普通一点吗，太容易误解了。

然后还要求线性复杂度，固定空间。

就想到了求和公式。哈哈。

理论值和实际值的差值就是缺少数的了。

有一个缺点就是有可能会overflow。

submit的结果为:
```
121 / 121 test cases passed.
Status: Accepted
Runtime: 60 ms
```

第二版用了异或。

思想是用该有的值和nums里的值逐一异或。剩下的就是缺少的了。

其实用求和也是一样，加上该有的然后减去nums里的。只是用求和有可能overflow。

submit的结果为:
```
121 / 121 test cases passed.
Status: Accepted
Runtime: 64 ms
```
