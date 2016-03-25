只需要一个有效解即可。

那就BFS然后记录一条路径即可。需要一个indegree数组，记录邻节点的入度。

当入度为0时加入queue，这也就是修完了所有前序课程的意思。

然后这个也可以防止环的出现，因为如果有环则无法进入该环，即无法完成其所需的前序课程。

submit的结果为:
```
36 / 36 test cases passed.
Status: Accepted
Runtime: 72 ms
```
