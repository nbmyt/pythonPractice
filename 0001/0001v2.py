#!/usr/bin/env python
# coding=utf-8

import string, random

class LengthError(ValueError):
    def __init__(self, arg):
        self.args = arg

def pad_zero_to_left(inputNumString, totalLength):
    """生成后四位主键， 主键数字从0开始递增， 需要保持4位，不足的位置补0"""
    lengthInputString = len(inputNumString)
    if lengthInputString > totalLength:
        LengthError("The length of in ")
    else:
        return '0' * (totalLength - lengthInputString) + inputNumString

keySheed = string.ascii_letters + string.digits
#生成随即的字符串
random_key = lambda x, y:"".join([random.choice(x) for i in range(y)])

def invitation_code_generator(quantity, length_random, length_key):
    #规定主键与随即字符串之间通过L连接
    placeHoldChar = "L"
    for index in range(quantity):
        tempString = ""
        try:
            yield random_key(keySheed, length_random) + placeHoldChar + \
                    pad_zero_to_left(str(index), length_key)
        except LengthError:
            print("Index exceeds the length of master key.")

for invitationCode in invitation_code_generator(200, 16, 4):
    print(invitationCode)
