"""
def string_bits(str):
    i = 0
    strcopy = ''
    while(i < len(str)):
        if i % 2 == 0:
            strcopy = strcopy + str[i]
        i = i + 1
    return strcopy

print(string_bits("Heeololeo"))
"""

def string_bits(str):
    result = ''
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result

print(string_bits("zhan"))


