#!/usr/bin/env python
#-*-coding: utf-8 -*-

def words(string):
    #s = unicode(string, 'utf-8')
    word_count = {}
    for word in string.split():
        if word_count.has_key(word):
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
    
print words('word')
print words("one of each")
print words("one fish two fish red fish blue fish")
print words('car : carpet as java : javascript!!&@$%^&')
print words('testing 1 2 testing')
print words('go Go GO')
print words('¡Hola! ¿Qué tal? Привет!')
print words('hello\nworld')
print words('hello  world')
