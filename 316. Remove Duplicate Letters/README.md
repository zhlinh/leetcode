第一版是比较容易想到的思路，即将每个字母的下标列成数组。

先遍历一遍s，就可以得到一个各字母按下标的大小排列的二维数组letters[26][]。

然后按字典序逐一添加。添加的位置letters[i][0]必须要小于等于所有字母的最大位置letters[i][-1]的最小值。

出现等于是因为某个letters[i]只有一个下标时有可能是它自身。

这样才能保证可以依序添加完所有字母，添加该字母后将该字母的下标数组置为空数组或None。
并记录添加的下标。

接下来就是从letters[i]中比所添加的下标要小的值，以保证依序添加。

以所有不重复字母的个数作为大循环。

如果认为O(26 * 26)的查找算是O(1)的话。

那么时间复杂度就是O(n)，耗费在删除所有字母的下标上。

submit的结果为:
```
286 / 286 test cases passed.
Status: Accepted
Runtime: 73 ms
```

第二版是递归的方法，思路与第一版稍有不同，会更清晰一些，但速度也会慢一些。

先计算每个字母的个数count，然后再遍历s，将当前字典序最小的位置作为pos。

每次都将字母的count减1，当有字母减到0时就break，因为count为0的字母表示没有重复项了。

再继续则有可能会错过该字母。

因为递归return的是s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ""))

即将pos的左侧全删掉，然后在pos的右侧中用replace删除掉与s[pos]相同的字母，进入下一层。

时间复杂度为O(n)。

submit的结果为:
```
286 / 286 test cases passed.
Status: Accepted
Runtime: 152 ms
```
