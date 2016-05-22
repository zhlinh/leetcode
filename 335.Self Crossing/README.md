看到这道题就想到了贪吃蛇。。。

数学题，得考虑到可以分为多少种碰撞情况。

步数小于3则直接返回False。


```
1. Fourth line crosses first line and onward

               i-2
    case 1 : i-1┌─┐
                └─┼─>i
                 i-3

2. Fifth line meets first line and onward

                    i-2
    case 2 : i-1 ┌────┐
                 └─══>┘i-3
                 i  i-4      (i overlapped i-4)

3. Sixth line crosses first line and onward

    case 3 :    i-4
               ┌──┐
               │i<┼─┐
            i-3│ i-5│i-1
               └────┘
                i-2

```

然后再分别写出i>=3, i>=4, i>=5的碰撞情况即可，先限制为该情况，再限制发生碰撞。

sumbmit的结果为:
```
29 / 29 test cases passed.
Status: Accepted
Runtime: 40 ms
```
