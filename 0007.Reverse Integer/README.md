感觉是道简单题，谁知道还有int范围限制的坑。

一开始用int->str->倒序->int。

觉得应该没啥问题，但谁知道int要是32位的。reverse后可能会超过限制，此时需要返回0。

所以改了下提交了第一版。

submit的结果为:
```
1032 / 1032 test cases passed.
Status: Accepted
Runtime: 52 ms
```

用了纯数学方法，这样比较通用。提交了第二版。

submit的结果为:
```
1032 / 1032 test cases passed.
Status: Accepted
Runtime: 56 ms
```
