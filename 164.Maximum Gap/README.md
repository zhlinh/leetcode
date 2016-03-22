第一版的解法是先找出min和max，然后将其分为N-1个格子。

除去min和max之外还有N-2个元素，扔到N-1个格子中至少会有一个格子是空的。

所以格子内的元素可以不用去比较。

也就是说maxGap会大于等于gap的。

gap = 1 + (max - min - 1) // (N - 1)。其实就是取ceil((max-min)/(N-1))。

然后再逐一当前的最小值减去前一个非空格子的最大值即可。

submit的结果为:
```
58 / 58 test cases passed.
Status: Accepted
Runtime: 48 ms
```
