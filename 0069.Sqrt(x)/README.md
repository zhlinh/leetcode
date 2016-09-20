最先想到的就是二分查找。

时间复杂度为O(log(n))。

submit的结果为:
```
1017 / 1017 test cases passed.
Status: Accepted
Runtime: 64 ms
```

第二版用了Newton Method(牛顿法)来解决。

牛顿法使用函数f(x)的泰勒级数的前面几项来寻找方程f(x)=0的近似根。

故有f(x) = f(x0) + (x - x0)f'(x0)。

以x0作为前一个点x[k]，而新求得的x为后一个点x[k+1]。

求解f(x) = 0得 x[k+1] = x[k] - f(x[k])/f'(x[k])

对于n^2 - x = 0，则有

n[k+1] = n[k] - (n^2 - x)/(2*x[k]) 

即：

n[k+1] = (1/2) * (n[k] + x/n[k])

submit的结果为:
```
1017 / 1017 test cases passed.
Status: Accepted
Runtime: 68 ms
```
