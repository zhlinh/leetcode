#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

words = ["Don't","go","around","saying","the","world","owes","you",
        "a","living;","the","world","owes","you","nothing;","it",
        "was","here","first."]
length = 4
sol = Solution()
res = sol.fullJustify(words, length)
print(res)
