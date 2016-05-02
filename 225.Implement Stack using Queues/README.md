pop和top都用了新的一个dequeue来存储popleft掉的元素。

submit的结果为:
```
16 / 16 test cases passed.
Status: Accepted
Runtime: 52 ms
```

第二版只用了一个dequeue。

只是重新将push重新定义成push到第一个元素，这样原先的popleft和top等函数就可以使用了。

push的方法为先将新元素append到最后，然后将旧元素逐一popleft再append到最后。

submit的结果为:
```
16 / 16 test cases passed.
Status: Accepted
Runtime: 36 ms
```
