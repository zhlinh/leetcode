第一版把上下移动和左右移动归为两类，然后赋值。

值得注意的最好是先移动坐标，再赋值，否则逻辑会很繁琐。

时间复杂度为O(m * n)

submit的结果为:
```
22 / 22 test cases passed.
Status: Accepted
Runtime: 52 ms
```

第二版用了一个dirs和一个step来保存方向及要走的步数，这样就可以很好地精简代码。

    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    step = [nc, nr]

时间复杂度为O(m * n)

submit的结果为:
```
22 / 22 test cases passed.
Status: Accepted
Runtime: 44 ms
```

还想到一个不断pop的思路，一行一列地往外pop。

不过时间复杂度可能会大于O(m * n)，所以就算了。
