""" Here you can find my solution for Kata 'Decode the Morse
Code, advanced', which you can find on link
https://www.codewars.com/kata/54b72c16cd7f5154e9000457 """
import re
def decodeBits(bits):
    pre_result = re.findall('1+|0+', bits.strip('0'))
    time = len(min(pre_result, key = lambda x: len(x)))
    result = ''
    for i in pre_result:
        if '1' in i:
            if i == '1'*3*time:
                result += '-'
            else:
                result += '.'
        else:
            if len(i) == 3*time:
                result += ' '
            elif len(i) == 7*time:
                result += '   '
    return result


