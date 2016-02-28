最先想到的就是计算0， 1， 2的个数，然后将之再顺序填入即可。

时间复杂度为O(n)。

submit的结果为:
```
86 / 86 test cases passed.
Status: Accepted
Runtime: 40 ms
```

第二版用了swap的方法。

值得注意的是交换后还需再检查一遍当前位置，此处用了while。

也可用i-=1的方式确保下一次检查当前位置。

时间复杂度为O(n)。

submit的结果为:
```
86 / 86 test cases passed.
Status: Accepted
Runtime: 52 ms
