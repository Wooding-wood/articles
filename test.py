# -*- coding: utf-8 -*-
# !/Users/lgf/anaconda/bin/python3
import sys
from collections import Counter
from math import sqrt, ceil

def valid_password(pwd):
    if(len(pwd) >=2 and len(pwd) <=10):
        if (pwd[0].isalpha()):
            if (pwd[-1].isalnum()):
                for c in pwd:
                   if(c.isalnum() or c=='_'):
                       return True
                   else:
                       print('char error')
                       return False
            else:
                print('[-1] error')
                return False
        else:
            print('[0] error')
            return False
    else:
        print('lenth error')
        return False


def prime_numbers():
    rag = 101
    result = []
    for i in range(2,rag):
        div = 2
        while (div <= ceil(sqrt(i))):
            if (i % div == 0 and div != i):
                break;
            div += 1
        else:
            result.append(i)

    print(result)


def letter_count(str):
    result = Counter(str)
    a = []
    for i in result:
        res = (i,result[i])
        a.append(res)
    return a

def cap_string(str):
    temp = str.split()
    res = ''
    for i in temp:
        res += (' ' + (i.capitalize()))
    return res

class Queue:
    buff = []

    def enqueue(self,add):
        Queue.buff.append(add)

    def dequeue(uadd):
        return Queue.buff.pop(0)

if __name__ == '__main__':
    a = sys.argv[1]
    #print(valid_password(a))
    #print(letter_count(a))
    #prime_numbers()
    #print(cap_string(a))

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

