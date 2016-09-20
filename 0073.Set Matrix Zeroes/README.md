第一版用了2个双重循环，第一遍寻找0的位置，记录行列，第二遍赋值。

时间复杂度为O(n^2)。

submit的结果为:
```
157 / 157 test cases passed.
Status: Accepted
Runtime: 192 ms
```

第二版还是2个双重循环，但没有用dict，真正的O(1) space。

值得注意的是最后赋值的时候逆序开始。

避免检查至第一行时，因col0=0而改变matrix[0][0]的值。

进而会改变row0的值，即使第一行不为0的时候。

进而会改变整个矩阵的值，故需要逆序[第一行，第一列存储状态]。

当然更容易理解的O(1)的思路是分别用第一行，第一列, row0， col0存储状态。

赋值的时候分3步： 除了第一行第一列的剩余矩阵， 第一行， 第一列。

submit的结果为:
```
157 / 157 test cases passed.
Status: Accepted
Runtime: 180 ms
```