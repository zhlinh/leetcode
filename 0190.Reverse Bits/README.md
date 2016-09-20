第一版就是逐比特取出然后加入到另一个整形中。

如果该函数被多次调用，用了一个dic来作优化，迅速返回已经求过的值。

submit的结果为:
```
600 / 600 test cases passed.
Status: Accepted
Runtime: 64 ms
```

第二版用的是每次都二分然后交换位置的方法，divide的思想。

在传入的unsigned int都是32位的情况下，可以做到O(1) space。

如果int的位数可变就得修改下程序，那就是O(log(size(int))) space。

该方法也是Java的JDK中Integer.reverse所用的方法。

submit的结果为:
```
600 / 600 test cases passed.
Status: Accepted
Runtime: 56 ms
```
