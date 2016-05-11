先用一个循环得出bull，并把secret的数字的个数作个统计。

然后再用一个循环找出guess中猜到的数字的个数，此结果包含cow和bull的总和。
用该结果减去bull就可以得出cow了。

当然还可以用两个数组分别统计secret和guess除了bull之外的的数字个数。
然后取两个数组的每个数字的最小值累加起来即为cow。

submit的结果为:
```
151 / 151 test cases passed.
Status: Accepted
Runtime: 100 ms
```

接下来就是别人家的孩子的show time了。

虽然时间复杂度是一样的，但是one pass，即只用了一个循环。

当不是bull时，计算cow用的是；
```
    if digits[int(secret[i])] < 0:
        cow += 1
    if digits[int(guess[i])] > 0:
        cow += 1
    digits[int(secret[i])] += 1
    digits[int(guess[i])] -= 1
```

即secret的数字个数作为+1，guess的数字个数-1。

这样就可以得出guess的数字以前secret遇到过，然后就会-1往0处靠拢，即中和掉该数字。
同时也可以得出secret的数字以前guess遇到过，然后就会+1往0出靠拢，即中和掉该数字。

如果未被中和掉，即非0，就是目前未匹配的数字。
正的表示未匹配的secret，负的表示未匹配的guess。

综合起来就是guess会去匹配secret以前的数字和未来的数字(换由secret来匹配guess来完成)。

这解法简直太聪明了。

另外用ord相减，即ASCII码运算代替了用int()转换，这样会快很多。

submit的结果为:
```
151 / 151 test cases passed.
Status: Accepted
Runtime: 68 ms
```
