第一版用了BFS。

每一次的queue里都加的是本行的元素。

就是间隔地要把level倒序，然后再添加到levels结果数组中。

submit的结果为:
```
33 / 33 test cases passed.
Status: Accepted
Runtime: 52 ms
```

第二版也是BFS，只是倒序的时候并不是等待本层结束时倒序。

而是在添加的是候每次都插入到第一个元素，这样与每次都append就形成了倒序。

基于此，一样可以用DFS的方法。

只需按depth%2来决定插入到本层第一个还是插入到本层最后即可。

submit的结果为:
```
33 / 33 test cases passed.
Status: Accepted
Runtime: 44 ms
```

第三版用了两个栈，这样就可以一个栈从加左到右，另一个从右加到左。

两个栈是交替为空的，需要注意的是最后一行的时候避免加入空数组。

submit的结果为:
```
33 / 33 test cases passed.
Status: Accepted
Runtime: 44 ms
```
