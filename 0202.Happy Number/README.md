第一版就是按照定义来解的。如果出现重复就退出循环，返回False。

符合条件就返回True。

submit的结果为:
```
400 / 400 test cases passed.
Status: Accepted
Runtime: 56 ms
```

第二版也是一样的思路，从定义解，只是把验证是否重复换成了slow和fast。

fast每次走两步，slow每次走一步。

哈哈，这个和循环链表类似。如果有圈，则fast一定会追上slow的。

值得注意的是需先判断是否为1再判断是否相等。

否则如果首次出现1，则后面再继续求平方和都会为1，这样会被误认为是重复返回false。

submit的结果为:
```
400 / 400 test cases passed.
Status: Accepted
Runtime: 54 ms
```

第三版利用到了一个数学规律，所有的unHappy的数都会进入到4开始的循环中。

所以只判断为1返回True，为4返回False即可。

4就是Happy number中的magic数。

submit的结果为:
```
400 / 400 test cases passed.
Status: Accepted
Runtime: 48 ms
```
