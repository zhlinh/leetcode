#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import WordDictionary

wordDictionary = WordDictionary()
wordDictionary.addWord("a")
wordDictionary.addWord("a")
print(wordDictionary.search("."))
print(wordDictionary.search(".a"))
print(wordDictionary.search("a."))
