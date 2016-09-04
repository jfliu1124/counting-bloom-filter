import hashlib
import math
import random

def gen_para(ft_len, b_num, p):
#   print('ft_len', ft_len)
    if ft_len:
        length = ft_len
        h_num = math.ceil(-(math.log(p)/math.log(2)))
    else:
        length = math.ceil(-(b_num* math.log(p))/((math.log(2)) ** 2))
        h_num = math.ceil((length/b_num)*math.log(2))
#       print(length, h_num)
    return length, h_num

def init_bf(length):   
    return [0] * length

def add_to_bf(val, vec, para):
    l = []
#   print(vec)
    for i in range(para[1]):
        loc = short_hash(val, para[0], i+1)
        l.append(loc)
#       print('loc ',loc)
        vec[loc] += 1
#   print(vec[loc],'plus 1, now is', )
    return vec

def short_hash(val, length, seed):
#   print('length is ', length)
    sha1 = hashlib.sha1()
    sha1.update(val.encode('utf-8'))
#   print(sha1.digest())
    val =  int(sha1.hexdigest(), 16) * seed
#   print('val',val%length)
    return val % length

def look_up(val, vec, para):
    print('enter look_up')
    for i in range(para[1]):
        loc = short_hash(val, para[0], i+1)   
        if vec[loc]:
            continue
        else:
            return False
    return True

def main():
    b_num, p = 50, 0.1
    para = gen_para(b_num, p)
    print(para)
    bloom_filter = init_bf(para[0])
    print(bloom_filter)
    while True:
        function = input("(查找（F）添加（A）退出（Q）查看（D）): ")
        if not function: break
        if function.lower() == 'q': break
        if function.lower() == 'a':
            buffer = input('input a string: ')
            bloom_filter = add_to_bf(buffer, bloom_filter, para)
        if function.lower() == 'f':
            buffer = input('input a string: ')
            print(look_up(buffer, bloom_filter, para))
        if function.lower() == 'd':
            print(bloom_filter)
    
if __name__ == '__main__': main()

