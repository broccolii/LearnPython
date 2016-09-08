#coding:utf-8
import locale
f = open('a.txt', 'r', encoding = 'utf8')
print(locale.getpreferredencoding())
print(f.read()) 