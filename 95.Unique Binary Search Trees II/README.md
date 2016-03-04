第一版用了递归。是DFS的思想但有根普通的DFS有所不同。

每一层都是一个新的trees、新的left，新的right。

tress只需要维护根节点，即有多少个根节点就有多少棵子树。

而左子树和右子树添加的都是一个节点，即某个子树的根节点。

left = ..., right = ...。返回的会是一个或多个子树的根节点。

以当前i值作为根节点，把left和right集合添加进来，形成不同的子树，添进trees中。

返回此trees，以此作为上一层的left或right。

submit的结果为:
```
9 / 9 test cases passed.
Status: Accepted
Runtime: 100 ms
```


第二版用了DP的方法。

初始化dp[0] = [None]。还需另外加判断n=0时返回[]，木有办法不然会返回[[]]。

即dp[i]可由本元素j + 1、左子树dp[j]和右子树dp[i-j-1]组成。

需要注意的是右子树dp[i-j-1]结构不变，但数值需要都加上j+1，才满足右边较大的条件。

j的范围从0到i-1遍历。

submit的结果为:
```
9 / 9 test cases passed.
Status: Accepted
Runtime: 96 ms
```
