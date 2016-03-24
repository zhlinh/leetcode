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

否则可能会出现追上的点恰好为1的情况，即出现1后会一直重复1。

submit的结果为:
```
400 / 400 test cases passed.
Status: Accepted
Runtime: 54 ms
```
