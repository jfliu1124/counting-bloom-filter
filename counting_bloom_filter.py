import hashlib
import math
import random
class Counting_bloom_filter(object):
    def __init__(self, el_num, p):
        self.el_num = el_num
        self.positive = p
        self.gen_para()
        self.init_bf()

    def gen_para(self):
        self.length = math.ceil(-(self.el_num* math.log(self.positive))/((math.log(2)) ** 2))
        self.hash_num = math.ceil((self.length/self.el_num)*math.log(2))

    def init_bf(self):   
        self.c_bf = [0] * self.length

    def add_to_cbf(self, val):

        for i in range(self.hash_num):
            loc = self.short_hash(val, i+1)

            self.c_bf[loc] += 1
            
    def delete(self, val):
        if self.look_up(val):
            for i in range(self.hash_num):
                loc = self.short_hash(val, i+1)
                self.c_bf[loc] -= 1
            print("delete success")
        else:
            print("ERROR:this element doesn't exist in bloom filter")
            
    def short_hash(self, val, seed):
        sha1 = hashlib.sha1()
        sha1.update(str(val).encode('utf-8'))
        val =  int(sha1.hexdigest(), 16) * seed
        return val % self.length

    def look_up(self, val):
        for i in range(self.hash_num):
            loc = self.short_hash(val, i+1)   
            if self.c_bf[loc]:
                continue
            else:
                print("Don't find", str(val))
                return False
        print("find", str(val))
        return True
def main():
    a = Counting_bloom_filter(3,0.001)
    print(a.c_bf)
    a.add_to_cbf(10)
    print(a.c_bf)
    print(a.look_up(2))
    a.delete(10)
    print(a.c_bf)
    a.delete(2)
    print(a.c_bf)    
if __name__ == '__main__': main()
