第一版用的是通用方法。

顺时针转90度: 先将矩阵的行逆序(reverse)，然后再求转置。

行逆序可以理解为将一张写着矩阵的纸向上(或下)翻转到背面。

求转置可以理解为沿主对角线斜向右上(或左下)翻转到正面。

这样就完成了顺时针转90度，可以观察某个顶点的位置变化来理解。

“翻转，然后如果在主对角线上则位置不变，其他位置移动到对角。”

时间复杂度为O(n^2)。

若为逆时针转90度，则先列逆序，然后再求转置。(或行逆序，然后沿次对角线转置)。

或者是先求转置，然后再行逆序。

submit的结果为:
```
20 / 20 test cases passed.
Status: Accepted
Runtime: 56 ms
```