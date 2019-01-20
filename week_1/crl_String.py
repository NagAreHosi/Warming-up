#String-1
#1
def hello_name(name):
  return "Hello %s!"%name
#2
def make_abba(a, b):
  return "%s%s%s%s"%(a,b,b,a)
#3
def make_tags(tag, word):
  return '<%s>%s</%s>'%(tag,word,tag)
#4
def make_out_word(out, word):
  return "%s%s%s"%(out[0:2],word,out[2:])
#5
def extra_end(str):
  return str[len(str)-2:]*3
#6
def first_two(str):
  if len(str)<2:
    return str
  else:
    return str[0:2]
#7
def first_half(str):
  return str[0:len(str)/2]
#8
def without_end(str):
  if len(str) == 2:
    return ""
  else:
    return str[1:-1]
#9
def combo_string(a, b):
  if len(a)>len(b):
    return b+a+b
  else:
    return a+b+a
#10
def non_start(a, b):
  return a[1:]+b[1:]
#11
def left2(str):
  if len(str) == 2:
    return str
  else:
    return str[2:]+str[0:2]

#String-2
#1
def double_char(str):
  s = ""
  for i in range(len(str)):
    s = s+str[i]*2
  return s
#2
def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i:i+2]=='hi':
      count += 1
      i += 2
  return count
#3
def cat_dog(str):
  catnum = 0
  dognum = 0
  for i in range(len(str)-2):
    if str[i:i+3] == 'cat':
      catnum += 1
      i += 3
    elif str[i:i+3] == 'dog':
      dognum += 1
      i += 3
  return catnum == dognum

#4
def count_code(str):
  count = 0
  for i in range(len(str)-3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
     count += 1
     i += 3
  return count
#5
def end_other(a, b):
  return a[-min(len(a),len(b)):].lower() == b[-min(len(a),len(b)):].lower()
#6
def xyz_there(str):
  for i in range(len(str)-2):
    if str[i:i+3] == 'xyz':
      if (i>0 and str[i-1]!='.') or i == 0:
        return True
  return False
