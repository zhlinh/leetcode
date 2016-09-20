第一版用了递归的思想。

求高度时只需考虑root.left是否为空，当只有一个节点时令高度为0，无元素时为-1。

高度h为负数时返回0，否则考虑root.right的高度，有两种情况。

情况1:
root.right的高度为h-1时，相当于与左子树的高度相等，说明root.left全为满的，
此时(1 << h, 即2的h次方)为root.left的全部节点和根节点的和，
然后再递归求root.right的节点数目即可。

情况2:
root.right的高度小于h-1时，说明root.right全为满的，但高度为h-2。
所以(1 << h-1, 即2的h-1次方))为root.right的全部节点和根节点的和，
然后再递归求root.left的节点数目即可。

因为求高度的时间复杂度为O(log(n))。

所以总的时间复杂度为O(log(n)^2)。

submit的结果为:
```
18 / 18 test cases passed.
Status: Accepted
Runtime: 220 ms
```
