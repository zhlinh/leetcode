第一版用的就解List的常用方法。

值得注意的是reverse的时候p的移动需一个tmp，p先往后移动，然后添加tmp到倒序序列。

submit的结果为:
```
44 / 44 test cases passed.
Status: Accepted
Runtime: 42 ms
```

第二版用了三个指针pre，start，then。

pre指向一开始之前的位置，逐步将then元素从链接中删除，然后移动到pre之后。

此时start相当于后移了一位，然后把then重新置为start之后。

移动时的代码各index都是首尾相连的。

submit的结果为:
```
44 / 44 test cases passed.
Status: Accepted
Runtime: 48 ms
```
