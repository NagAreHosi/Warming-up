#String-1
#1
def hello_name(name):
    return 'Hello ' + name + '!'

#2
def make_abba(a, b):
    return a + b + b + a

#3
def make_tags(tag, word):
    return '<{0}>{1}</{2}>'.format(tag, word, tag)

#4
def make_out_word(out, word):
    return out[:2] + word + out[-2:]

#5
def extra_end(str):
    return  str[-2:] * 3

#6
def first_two(str):
    return str[0:2]

#7
def first_half(str):
    return str[:len(str)/2]

#8
def without_end(str):
    return str[1:len(str)-1]

#9
def combo_string(a, b):
    if len(a) > len(b):
        return '{0}{1}{2}'.format(b, a, b)
    else:
        return '{0}{1}{2}'.format(a, b, a)

#10
def non_start(a, b):
    return a[1:] + b[1:]

#11
def left2(str):
    if len(str) > 2:
        return str[2:] + str[:2]
    return str

#String2
#1
def double_char(str):
    s = ''
    for i in range(len(str)):
        s += str[i] * 2
    return s

#2
def count_hi(str):
    count = 0
    index = 0
    while 'hi' in str:
        index = str.find('hi')
        str = str[:index] + str[index+2:]
        count += 1
    return count

#3
def cat_dog(str):
    c = 0
    d = 0
    while 'cat' in str:
        n = str.find('cat')
        str = str[:n] + str[n+3:]
        c += 1
    while 'dog' in str:
        n = str.find('dog')
        str = str[:n] + str[n+3:]
        d += 1
    return c == d

#4
def count_code(str):
    count = 0
    while 'co' in str:
        n = str.find('co')
        if n+3 > len(str)-1:
            return count
        if str[n+3] == 'e':
            count += 1
            str = str[:n] + str[n+4:]
        else:
            str = str[:n] + str[n+2:]
    return count

#5
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return (a in b and b.find(a, -len(a)) >= 0) or (b in a and a.find(b, -len(b)) >= 0)

#6
def xyz_there(str):
    while '.' in str:
        n = str.find('.')
        if str[n:n+4] == '.xyz':
            str = str[:n] + str[n+4:]
        else:
            str = str[:n] + str[n+1:]
    return 'xyz' in str
