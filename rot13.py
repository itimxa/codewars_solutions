"""Here you can find my solition for Kata Rot13,
you can find task by using link below
https://www.codewars.com/kata/rot13-1"""

import string
from codecs import encode as _dont_use_this_

def rot13(message):
    res = ""
    for i in message:
        if i.isalpha():
            if ord(i) > 109:
                res += chr(97 + 12 - 122 + ord(i))
            elif ord(i) > 77 and i.isupper():
                res += chr(65 + 12 - 90 + ord(i))
            else:
                res += chr(ord(i) + 13)
        else:
            res += i
    return res
