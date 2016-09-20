用到了Segment Tree分段数，又称为Binary Indexed Trees。

比一般的树节点多了两个变量，start和end，然后用val来记录数组从start到end的和。

而且本节点的值等于左子树的值加上右子树的值。

左子树保存的是从start到mid的值，而右子树保存的是从mid+1到end的值。

其中mid = start + (end - start) // 2。

这样更新一个叶子节点的值，只需更新从根节点到叶子节点经过的节点即可，
复杂度为O(log(n))。

而计算从某个i到某个j(i <= j)的和所需要的时间也是O(mlog(n))。

计算和的时候如果是j <= mid，就进入到左子树中计算。
如果是i > mid，就进入到右子树中计算。
横跨两个子树的情况就到左子树中计算i到mid，
到右子树中计算mid+1到j的值，返回两个的和。

submit的结果为:
```
10 / 10 test cases passed.
Status: Accepted
Runtime: 628 ms
```

第二版就是纯粹的用数组的index来构建树，也就是binary Indexed Trees（BIT）。

详见[Topcoder-BIT](https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/)

注意看黑体字和图片就好。

关键的点有两点：

`问题一`是构建的累加和数组c[i]只表示(i-2^r，去掉最后一个1)到i的和，不包括i。
比如c[110]表示f[100]和f[101]的和。
f表示frequency频度，也就是输入的nums。
所以为了方便，数组c会比原来数组f的长度多1，这样就可以写成：

```
Bit: 1 -> 0
self.c[1] = nums[0]

Bit: 10 -> 00 + 01
self.c[2] = nums[0] + nums[1]

Bit: 11 -> 10
self.c[3] = nums[2]

Bit: 100 -> 000 + 001 + 010 + 011
self.c[4] = nums[0] + nums[1] + nums[2] + nums[3]

Bit: 101 -> 100
self.c[5] = nums[4]

Bit: 110 -> 100 + 101
self.c[6] = nums[4] + nums[5]

Bit: 111 -> 110
self.c[7] = nums[6]

Bit: 1000 -> 0000 + 0001 + 0010 + 0011 + 0100 + 0101 + 0110 + 0111
self.c[8] = nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5] \
            + nums[6] + nums[7]
```

可以看出二进制bit位末尾为1的，都只有1个数，因为末尾为1时只有末尾为0到自身的和，
且不包括自身。

二进制为2的幂时，即二进制bit位置只有一个1时，都是从0到自身的和，不包括自身。

其他情况都是分段的。

即都是去掉二进制最低位的1的数到本身的和(不包括本身)。

最低位的1可以由式子(k & -k)得出，-k表示取反加1。

即(k & -k) = a1(n个0) & ((^a)0(n个1) + 1) = a1(n个0) & ((^a)1(n个0) = 1(n个0)。

这个是计算最低位的1的常用式子。哈哈，相当巧妙。

所以 k += (k & -k)

有了nums[i]会被哪个c[k]累加，就可以初始化数组c了。
update的话和初始化一样，改变nums[i]值，然后算出diff来改变包含nums[i]的c[k]。
而算出nums从i到j的和，就可以用0到j的和减去0到i-1的和。

`问题二`来了，如何计算0到i的和。
其实就是考虑nums[i]不在哪些c[k]中。

比如计算nums从0到6的和，sum[b’110] = c[b’111] + c[b’110] + c[b’100]。

看出来了吗，计算6时需要以c[7]作为开始，这个已经说过，因为c[0]相当于是空的，
下标比nums多1。
比较方便计算。当然从定义也很容易知道，因为不包含自身，c[i+1]的总会包含nums[i]。

然后就不断地去除自己末尾的1，即不断减去最低位的1，直到只有1位为1的时候。

上面已经说过，只有1位为1的时候，正是从0加到自身，不含自身的时候。

定义c的时候只会消耗掉自己末尾的1个1。而不断地消耗自己的1直到只有1个1为止，
则是不断把求和的范围往前面的一段靠，直到算出从0到自身，不包含自身的和。

此时c[k]的 k -= (k & -k)。

这样就完成了求和。

submit的结果为:
```
10 / 10 test cases passed.
Status: Accepted
Runtime: 196 ms
```
