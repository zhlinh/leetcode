#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Trie

trie = Trie()
trie.insert("somestring")
print(trie.search("some"))
print(trie.startsWith("some"))
print(trie.search("somestring"))
