第一版用了后序遍历的循环写法。

需要注意的是后序遍历一开始会为取栈最上面的值，而不要pop。

直到无右子树或右子树为前一个遍历的节点时才pop。

另外需要注意的是需要始终需要将cur赋值，即使在cur.right为空或类似空时。

这样才能将栈顶部的值再次取出。

submit的结果为:
```
67 / 67 test cases passed.
Status: Accepted
Runtime: 48 ms
```
