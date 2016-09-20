第一版用了递归解法。

可以看先序的第一个即为root，然后找到中序所在的位置，其左右各为左子树和右子树。

先序的root的下一个个即为左子树的root。

然后由中序确定当前左子树的个数，在先序中往后移找到右子树的root。

依次递归，将所有的root确定。无子节点时返回None。

subimt的结果为:
```
202 / 202 test cases passed.
Status: Accepted
Runtime: 432 ms
```

第二版改进了下第一版。

用了一个dic来存储inoder的index，方便查找所在位置。将查找的O(n)降为O(1)。

当然需要先初始化dic。

subimt的结果为:
```
202 / 202 test cases passed.
Status: Accepted
Runtime: 80 ms
```

第三版用了循环的方法。比递归法要快。不过可能理解起来需要点时间。

以preorder作为主循环。

用了一个stack存preinoder的之前节点，用了一个int存inordr的当前位置。

相当赞的思路。

subimt的结果为:
```
202 / 202 test cases passed.
Status: Accepted
Runtime: 60 ms
```
