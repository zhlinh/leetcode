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

第二版用了DFS。

将每个元素加入到对应的层级中，进入新的更深的一层则先扩充List。

submit的结果为:
```
34 / 34 test cases passed.
Status: Accepted
Runtime: 56 ms
```
