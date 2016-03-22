一开始就想到用中序遍历然后把结果都存下来，哈哈。

这样O(1) time没问题，但就成了O(n) space。

后来看了别人的答案，也是用栈，但一开始只压入左子树。

当访问了next之后，又从该节点的右子树开始将左子树压入堆栈。

这就是将中序遍历的循环模式分为两部分。next相当于访问了中间节点。

然后将右子树作为cur，接着循环将左子树压入堆栈。

这样实现next为O(h) space，但为O(h) time。

[也有人说每个节点最多访问两次，平均也算O(1) time的]

hasNext为O(h) space, O(1) time没问题。

submit的结果为:
```
61 / 61 test cases passed.
Status: Accepted
Runtime: 112 ms
```
