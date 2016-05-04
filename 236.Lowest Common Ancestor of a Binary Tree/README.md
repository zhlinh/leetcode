真的是见识到了神一般的递归。

用的思想是后序遍历，然后如果找到其中一个则将该节点return到最前。

此时返回可能存在另一个但并没有继续往下找，因为没必要。
因为如果找不到返回的会是找到的一个，也会是正确答案。

如果同时找到两个则返回的是它们最近的父节点。也就是题目所求。

submit的结果为:
```
31 / 31 test cases passed.
Status: Accepted
Runtime: 132 ms
```

第二版用循环的方式来实现上述递归。

这也是很赞的思路。

构建了另一个类，Frame，其实是通用的stack frame的思想。

用来保存parent父节点的Frame信息，还有sub子节点是否找到p或q节点的信息。

也是后序遍历。

先找到最左的节点，然后将两个None作为Frame压入stack中。

然后将最左节点的sub分别填入两个None，stack中依次pop掉None的Frame。

接着就可以在最左节点的parent父节点Frame的sub中填入None，即sub[0]为左子树的输出。

如果是找到了p或q的话，则会将p或q填入相应的父节点Frame的sub中。

sub[0]为左子树，sub[1]为右子树。这是由stack先压入node.right，再压入node.left决定的。

如果压入顺序相反，则sub[0]和sub[1]表示的含义也相反

当然这个是无所谓的，因为最终的root中的左右子树sub[0]和sub[1]信息会汇总给root的虚头结点answer的sub中，
answer的sub有且只有一个sub[0]。

submit的结果为:
```
31 / 31 test cases passed.
Status: Accepted
Runtime: 216 ms
```
