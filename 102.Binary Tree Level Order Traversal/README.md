第一版用了BFS。

每一次的queue里都加的是本行的元素。

然后以queue的长度为界，循环地pop到level里，另外再添加新的左右子树到queue里。

关键就是要知道本行的元素个数。这样才可以分层。

submit的结果为:
```
34 / 34 test cases passed.
Status: Accepted
Runtime: 52 ms
```
