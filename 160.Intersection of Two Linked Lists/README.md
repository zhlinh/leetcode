用了求带循环圈链表的开始点的求法，先将A和B首尾相连。

然后再求是否存在圈再将起始点给出。

需要注意的是返回时需要将AB给断开。

然后另外一点是确定有圈然后求起始点时需要先判断然后再下一跳。

因为有可能该圈是从一开始就循环了的。

submit的结果为:
```
42 / 42 test cases passed.
Status: Accepted
Runtime: 344 ms
```

第二版的方法更加直接。

用了一个事实如果有相交的话h1走完headA然后走headB和h2走完headB再走headA。

走到交点时所用的步数是一样的，即都走过了对方走过的路，此时h1会等于h2。

返回h1即可。

当然如果无交点，那就相当于h1和h2都走完了headA和headB，此时最后两个也都为None。

此时也是相等，返回h1，也就是None。

不直接返回None，是因为有headA直接等于headB的情况，即一开始就相交。

submit的结果为:
```
42 / 42 test cases passed.
Status: Accepted
Runtime: 409 ms
```
