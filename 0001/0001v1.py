#!/usr/bin/env python
# coding=utf-8

import string, random

key_speed= string.ascii_letters + string.digits

def getKey(key_length, key_nums):
    for i in range(key_nums):
        key = ""
        for j in range(key_length):
            key +=random.choice(key_speed)
            if j % 4 == 3 and j != 15:
                key += "-"
        print(key)

if __name__ == "__main__":
    getKey(16, 200)



