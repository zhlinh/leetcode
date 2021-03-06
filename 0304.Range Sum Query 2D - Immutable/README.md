第一版就把矩阵折成线性的然后算从最左上元素到当前元素的线性和。

然后就可以求每一行的和。

最后相加。

求和的时间复杂度为O(n)。

submit的结果为:
```
12 / 12 test cases passed.
Status: Accepted
Runtime: 304 ms
```

第二版就利用率从00到ij的矩阵的和，然后就可以用O(1)来求和。

初始化时利用的是：

```
    self.from00Sum[i+1][j+1] = self.from00Sum[i+1][j] + \
        self.from00Sum[i][j+1] - self.from00Sum[i][j] + matrix[i][j]
```

用图来表示就是：

```
+-----+-+------+     +--------+-----+     +-----+---------+     +-----+--------+
|     | |      |     |        |     |     |     |         |     |     |        |
|     | |      |     |        |     |     |     |         |     |     |        |
+-----+-+      |     +--------+     |     |     |         |     +-----+        |
|     | |      |  =  |              |  +  |     |         |  -  |              |
+-----+-+      |     |              |     +-----+         |     |              |
|              |     |              |     |               |     |              |
|              |     |              |     |               |     |              |
+--------------+     +--------------+     +---------------+     +--------------+

                        +-----+-+------+
                        |              |
                        |              |
                        +     +-+      |
                     +  |     | |      |(即matrix[i][j])
                        +     +-+      |
                        |              |
                        |              |
                        +--------------+

注意最右下角就是matrix[i][j]，即新增的元素，这样就可以逐一初始化from00Sum。
```

然后求解时就类似求matrix[i][j]，把等式只不过此时最右下角变成了一个范围。
但原理是一样的，就是最左上角会被重复减掉，最后再加上即可。

即：

```
    self.from00Sum[row2+1][col2+1] - self.from00Sum[row2+1][col1] \
           - self.from00Sum[row1][col2+1] + self.from00Sum[row1][col1]
```

总结一下就是一维的话就直接从原点拉出宽度为1的矩阵即可。

而二维就是从原点拉出一个矩阵(之前已由DP方法初始化的)，
然后设法剪掉其他由原点拉出来的部分即可，注意会重复剪掉左上角，最后记得要加上。

submit的结果为:
```
12 / 12 test cases passed.
Status: Accepted
Runtime: 80 ms
```
