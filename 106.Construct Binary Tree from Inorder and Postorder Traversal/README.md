第一版用了递归解法，还初始化了一个inorder的dic作查询位置用。

postorder倒序，即可认为是中-右-左。

这样就可以用preorder和inorder类似的方法解了。

然后从postorder最后一个开始作为root，递归划分右子树和左子树。

subimt的结果为:
```
202 / 202 test cases passed.
Status: Accepted
Runtime: 72 ms
```

第二版改成了循环法。

从postorder的最后一个开始往前循环。

subimt的结果为:
```
202 / 202 test cases passed.
Status: Accepted
Runtime: 60 ms
```
