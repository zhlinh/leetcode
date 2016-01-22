第一版用了递归的方法，DFS(深度优先搜索)。

submit的结果为:
```
8 / 8 test cases passed.
Status: Accepted
Runtime: 44 ms
```

第二版看了别人的答案，用到了DP(动态规划)。

相当赞啊。

关键要理解新的结果生成是由前面的结果得来的，即可分解为子问题。

例如:

n=0, res(n=0) = ‘’

n=1，res(n=1) = ‘()’

n=2, 可分解为‘(‘ + res(n=0) + ‘)’ + res(n=1) 和 ‘(’ + res(n=1) + ‘)’ + res(n=0)

n=3，可分解为‘(‘ + res(n=0) + ‘)’ + res(n=2) , ‘(’ + res(n=1) + ‘)’ + res(n=1)
           和‘(‘ + res(n=2) + ‘)’ + res(n=0)

或者是res(i) + ( res(n-1-i) )的形式也可以，前缀后缀均可，统一用一种就行。

submit的结果为:
```
8 / 8 test cases passed.
Status: Accepted
Runtime: 44 ms
```
