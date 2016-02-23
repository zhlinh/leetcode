第一版需要将intervals先按起点排序。

然后再逐一判断。

时间复杂度为O(n)。

sbumt的结果为:
```
168 / 168 test cases passed.
Status: Accepted
Runtime: 108 ms
```

第二版根据intervals的起点已排序的特点精简了下代码。

去掉了后一个的end要大于前一个的start的判断，

去掉修改前一个的start。

去掉了新生成一个Interval。

时间复杂度为O(n)。

sbumt的结果为:
```
168 / 168 test cases passed.
Status: Accepted
Runtime: 80 ms
```
