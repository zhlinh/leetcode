这个理解起来挺复杂的，有点数电的意思，哈哈。就是运用比特的思维。

把数字int也当成一个比特来理解。

现在要求的是出现三次中找出出现一次的。所以三次就是11。

所以需要用两个比特，即两个int，将其命名为x1, x0。

x1 = x1 ^ (x0 & num[i])，即只有x0低位和num[i]都为1的时候才会进位，x1才会有改变。

x0 = x0 ^ nums[i]，这个就比较好理解了，比特加法的概念。

然后需要注意的是mask，就是要让满足3次的时候x1和x0变为0。其他情况就不管了。

这样你就会想到如果是出现求四次中找出现一次的话，就不用这个mask了。

因为出现四次时，x1和x0会自动变为0，比特加法，100，嘿嘿。

然后这个mask的确定就是按出现的次数，出现3次变为0，则mask = ~(x1 & x0)。

这个可以理解吧，就是11取反，然后x1 = mask & x1 和x0 = mask & x0就可以让其都变为0了。

然后循环完nums[i]，返回x0就可以了。

这个是通用的解法，解决从出现两次的中找出现一次的也是一样的思路，只是不用mask了。

更详细的解释见:

[LeetCode-Detailed explanation and generalization of the bitwise operation method for single numbers](https://leetcode.com/discuss/31595/detailed-explanation-generalization-bitwise-operation-numbers)

> 相关扩展

如果题意是求出现三次中找出其中一个出现不同次数的(具体次数不限，但不为三的倍数)。

是这样的话可以用32个比特逐一匹配。外层循环为32个比特的位置。

内层循环为nums的个数，然后相与，计算出出现1的次数，用得到的次数取3的余数。

若不为0，则用res与该比特位置相或，即赋该位置为1。

这也是一种简单且直观的解法。

sumbmit的结果为:
```
11 / 11 test cases passed.
Status: Accepted
Runtime: 52 ms
```
