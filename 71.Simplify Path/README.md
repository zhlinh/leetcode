第一版试了挺多遍的。

原来除了需要考虑/.和/..之外，还需要在pop的时候考虑res是否为空。

还需要考虑append的时候str是否为空，是否为/。

最后返回的时候若为空则返回“/”。当然一开始要排除path为空的情况。

然后终于accepted了。

submit的结果为:
```
252 / 252 test cases passed.
Status: Accepted
Runtime: 68 ms
```
