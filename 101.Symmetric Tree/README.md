第一版用了递归前序遍历，分为两个部分作镜面比较。

submit的结果为:
```
192 / 192 test cases passed.
Status: Accepted
Runtime: 60 ms
```

第二版用了循环的前序遍历，左子树为中-左-右，右子树为中-右-左。

共用一个stack即可。

submit的结果为:
```
192 / 192 test cases passed.
Status: Accepted
Runtime: 52 ms
```
