看到O(n) Time和O(1) Space就想到了分为前后两段，然后将后半段倒序。

这样就可以进行逐一比较了。但效果不是很好。挺耗时的，哈哈。

submit的结果为:
```
21 / 21 test cases passed.
Status: Accepted
Runtime: 276 ms
```

第二版为更简洁的写法，因为倒序时只颠倒了箭头的方向，而不是采用逐一移动到最前的倒序方法。

而且倒序前半部分，在寻找中点时同时进行。

并在判断是否为回文时恢复原来的ListNode，虽然没作要求，但破坏原结构感觉不太好。

submit的结果为:
```
21 / 21 test cases passed.
Status: Accepted
Runtime: 156 ms
```
