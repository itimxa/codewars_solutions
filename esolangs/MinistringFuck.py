"""This is solution for first Kata from Esolang series
task you can find on the link below
https://www.codewars.com/kata/586dd26a69b6fd46dd0000c0"""

def my_first_interpreter(code):
    counter = 0
    result = ''
    for i in code:
        if i == "+":
            counter += 1
            if counter == 256:
                counter = 0
        elif i == ".":
            result += chr(counter)
    return result
