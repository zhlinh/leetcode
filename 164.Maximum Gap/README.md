第一版的解法是先找出min和max，然后将其分为N-1个格子。

除去min和max之外还有N-2个元素，扔到N-1个格子中至少会有一个格子是空的。

所以格子内的元素可以不用去比较。

也就是说maxGap会大于等于gap的。

gap = 1 + (max - min - 1) // (N - 1)。其实就是取ceil((max-min)/(N-1))。

然后再逐一当前的最小值减去前一个非空格子的最大值即可。

submit的结果为:
```
17 / 17 test cases passed.
Status: Accepted
Runtime: 72 ms
```

第二版的解法用了Radix-Sort。当然该解法并没有第一版好。

因为是需要先排序，排序的方法是逐一比较每一位的数字。

计算0~9的数目放入count数组中。然后将count数组的当前元素与前面一个元素累加。

这样就得到了当前位置的index值的终点。

最后一个count即9的index值的终点为Nums的长度。

就可以将nums从后往前根据其所在的区间然后放入(count-1)值作为index的另一个数组中。

从后往前是因为要利用上一次的排序位置。

然后再将该数组赋值给nums。完成一次排序。

接着循环更高位的数字。循环次数为最大值的位数。

最终得到的另一个数组即为由小到大排序好的数组。

submit的结果为:
```
17 / 17 test cases passed.
Status: Accepted
Runtime: 100 ms
```
