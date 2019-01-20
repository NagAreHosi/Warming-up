# -*- coding: utf-8 -*-
#1
def hello_name(name):
  return ("Hello "+name+"!")

#2
def make_abba(a, b):
  return (a+b*2+a)

#3
def make_tags(tag, word):
  return ('<'+tag+'>'+word+'</'+tag+'>')

#4
def make_out_word(out, word):
  return (out[:2]+word+out[2:])

#5
def extra_end(str):
  s=str[len(str)-2:]
  return s*3

#6
def first_two(str):
  return (str[:2])

#7
def first_half(str):
  return (str[:len(str)/2])

#8
def without_end(str):
  return (str[1:len(str)-1])

#9
def combo_string(a, b):
  if len(a)==0 or len(b)==0:
    return a+b
  else:
    s = a if len(a)<len(b) else b
    t = b if len(b)>len(a) else a
    return s+t+s

#10
def non_start(a, b):
  return a[1:]+b[1:]

#11
def left2(str):
  return str[2:]+str[:2]
