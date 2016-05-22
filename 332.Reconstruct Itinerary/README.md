一看就知道很明显的DFS，但还是有一定技术含量的。

算是典型的图的路径问题。

关键是要不断减少节点的出度，然后遇到出度为0的时候将节点加入DFS。

从顶部往下DFS，从底部往上添加res。

先建立一个dic，初始化图，即记录下一跳的节点。

注意得给tickets先逆序排序，以保证dic[key][-1]是字典序较小的。

然后可以用递归或stack循环执行DFS。

思路是:

1. 初始化stack = [“JFK”]。

2. 不断地往前进，并在其邻接矩阵中pop掉所前进的这一跳，加入到stack中，
退出while的条件是遇到出度为0的。

3. 若遇到出度为0则将该节点就加入res中，并在stack中pop掉当前节点。

4. 返回res[::-1]即为题目所求。

sumbmit的结果为:
```
79 / 79 test cases passed.
Status: Accepted
Runtime: 96 ms
```
