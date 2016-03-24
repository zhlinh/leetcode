先计算其跨度所处的2的幂指数范围。

如1->0; 2->1; 3,4->2; 5,6,..8->3。。。

其表示最末的几位为0，并以此作为mask。然后只需返回起点&终点&mask即可。

submit的结果为:
```
8266 / 8266 test cases passed.
Status: Accepted
Runtime: 212 ms
```
