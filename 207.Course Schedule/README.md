第一版用的BFS，对于topological sort需要用一个数组表示每个顶点的入度。

为了避免重复此处用了一个set，防止同一条边重复。

当然用arraylist也是可以的，一直添加边，然后入度一直增，只是会增加访问次数。

BFS开始后，每次count加1，访问每个邻节点，邻节点的入度减1。

当其入度恰好为0的时候将该邻节点加入到queue中。

举个例子[0->1->2->3,4->5->3]。

初始化时会将入度为0的0和5节点加入queue，3的入度为2。

所以当2想要访问3的时候并没有将3加入到queue，只是将3的入度减1。

然后另一条路径由5顺利访问3。

这样很好地避免了循环访问，即每个节点只被添加到queue中一次。

且如果在中途有环，直接进入不了该环而退出循环。

submit的结果为:
```
35 / 35 test cases passed.
Status: Accepted
Runtime: 64 ms
```

第二版用了DFS，为了避免重复访问用了一个visited。

因为要在主函数中多次调用该DFS，所以visited有3个值。

0表示未访问过，1表示此次DFS访问过，用来查看是否有环，-1表示全局已经访问过。

这样下次DFS的时候只需访问visited为0的点即可。

在DFS中若邻节点的visited为1则返回False，表示有环，即可得答案。

如果访问完所有节点无环则返回True。

哈哈，本来还想改成在主函数由indegree入度为0的点作为起点来调用DFS。

后来发现是行不通的，因为如果是环则会错过，同时又有其他单向链，无法定义flag来判断。

BFS可行是因为有count，如果count不等于课程的数目则返回false。

好吧，当然你也可以定义一个count，然后DFS。

submit的结果为:
```
35 / 35 test cases passed.
Status: Accepted
Runtime: 68 ms
```