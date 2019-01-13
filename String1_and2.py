#String-2
#1
def hello_name(name):
    return "Hello " + name + '!'

#2
def make_abba(a, b):
  return a + b + b + a

#3
def make_tags(tag, word):
  a = '<' + tag + '>'
  b = '</' + tag + '>'
  return a + word + b

#4
def make_out_word(out, word):
  return out[:2] + word + out[2:]

#5
def extra_end(str):
  return str[len(str) - 2:len(str)] * 3


#6
def first_two(str):
  if len(str) < 2:
    return str
  else:
    return str[0:2]

#7
def first_half(str):
  return str[0:len(str)/2]

#8
def without_end(str):
  return str[1:len(str) - 1]

#9
def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  return a + b + a

#10
def non_start(a, b):
    if len(a) == 1 and len(b) != 1:
        return b[1:len(b)]
    if len(a) != 1 and len(b) == 1:
        return a[1:len(a)]
    return a[1:len(a)] + b[1:len(b)]

#11
def left2(str):
    return str[2:len(str)] + str[0:2]

#String-2
#1
def double_char(str):
    str2 = ''
    for i in range(len(str)):
        str2 = str2 + str[i] * 2
    return str2

#2
def count_hi(str):
    return str.count('hi',0,len(str))

#3
def cat_dog(str):
    if str.count('cat',0,len(str)) == str.count('dog',0,len(str)):
        return True
    return False

#4
def count_code(str):
    list1 = list(str)
    for i in range(len(list1)):
        if list1[i] != 'c' and list1[i] != 'o' and list1[i] != 'e':
            list1[i] = 'd'
        else:
            continue
    str = "".join(list1)
    return str.count('code', 0, len(str))

#5
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if len(a) > len(b):
        if a.find(b, len(a) - len(b), len(a)) != -1:
            return True
        else:
            return False
    else:
        if b.find(a, len(b) - len(a), len(b)) != -1:
            return True
        else:
            return False

#6
def xyz_there(str):
    strsplit = str.split('.')
    if 'xyz' in strsplit[0]:
        return True
    for i in strsplit:
        if len(i) >= 3:
            if i.count("xyz", 1, len(i)) != 0:
                return True
    return False
