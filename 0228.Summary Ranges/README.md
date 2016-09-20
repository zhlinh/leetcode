就是用了一个start和end来记录始末位置的思路。

初始化start为int最大值，end为int最小值。

需要注意的是最后还需添加一次str，因为是滞后判断。

还有nums为空时应直接返回[]。

submit的结果为:
```
27 / 27 test cases passed.
Status: Accepted
Runtime: 44 ms
```

第二版更简洁一些，只记录start，然后是提前判断。nums[i+1]-nums[i]是否等于1。

submit的结果为:
```
27 / 27 test cases passed.
Status: Accepted
Runtime: 48 ms
```
