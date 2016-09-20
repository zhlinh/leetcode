想到了2倍的关系，即最合适的组合方式是[1, 2, 4, 8]这样的组合，定为top。

符合nums[i]<=top的时候一开始我以为就`top *= 2`，`i += 1`。这样想就错了。
应该是`top += nums[i]`，`i += 1`。
因为符合的时候可能并不是最佳的数，所以达不到最佳的top*2。

如果不符合的时候，即`i >= len(nums) or nums[i] > top`就`res += 1`，然后top*=2，

退出循环的条件是`top > n`。

sumbmit的结果为:
```
149 / 149 test cases passed.
Status: Accepted
Runtime: 64 ms
```
