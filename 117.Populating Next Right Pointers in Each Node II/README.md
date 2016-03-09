第一版用了三个指针。

分别指向上一层的元素，本层第一个元素，本层的元素。

然后就是简单的拼接了。注意在本层中的左右节点也当做相隔的来处理。

即拼接利用的是pre.next = cur.left(right)。

然后当pre为None时，就可以确定本层的第一个元素head。

```
61 / 61 test cases passed.
Status: Accepted
Runtime: 104 ms
```
