def hello_name(name):
  return "Hello " + name + '!'
  
  
  
  def make_abba(a, b):
  return a + b + b + a

  
  def make_tags(tag, word):
  a = '<' + tag + '>'
  b = '</' + tag + '>'
  return a + word + b

  
  
  def make_out_word(out, word):
  return out[:2] + word + out[2:]
  
  def extra_end(str):
  return str[len(str) - 2:len(str)] * 3

  
  def first_two(str):
  if len(str) < 2:
    return str
  else:
    return str[0:2]

	
	
	def first_half(str):
  return str[0:len(str)/2]
  
  
  
  
  def without_end(str):
  return str[1:len(str) - 1]

  
  
  
  def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  return a + b + a

  
  
  
  def non_start(a, b):
    if len(a) == 1 and len(b) != 1:
        return b[1:len(b)]
    if len(a) != 1 and len(b) == 1:
        return a[1:len(a)]
    return a[1:len(a)] + b[1:len(b)]
	
	
	
	
	def left2(str):
    return str[2:len(str)] + str[0:2]
