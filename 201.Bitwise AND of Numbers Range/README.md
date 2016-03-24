先计算其跨度所处的2的幂指数范围。

如1->0; 2->1; 3,4->2; 5,6,..8->3。。。

其表示最末的几位为0，并以此作为mask。然后只需返回起点&终点&mask即可。

submit的结果为:
```
8266 / 8266 test cases passed.
Status: Accepted
Runtime: 212 ms
```

第二版用的是n &= (n - 1)，循环直到m >= n退出。然后返回n。

如果n==m很容易理解n即为所求。

而n<m，举个例子就是11和100，然后n最后为0，n<m，n为所求。

submit的结果为:
```
8266 / 8266 test cases passed.
Status: Accepted
Runtime: 192 ms
```

第三版是m >>= 1，n >>= 1， shift += 1。直到m == n退出循环。然后返回n << shift。

这个就比较容易理解了，将m和n不相同的置0即为所求。

submit的结果为:
```
8266 / 8266 test cases passed.
Status: Accepted
Runtime: 208 ms
```
