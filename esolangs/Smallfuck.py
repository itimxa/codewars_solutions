"""My second solution for Kata from Esolang series
you can find full task description by link below
https://www.codewars.com/kata/58678d29dbca9a68d80000d7"""


def interpreter(code, tape):
    tape = list(tape)
    change = {'1': '0', '0': '1'}
    marker = i = 0
    while i != len(code) and len(tape) > marker >= 0:  # check conditions to termination
        if code[i] == '>':
            marker += 1
        elif code[i] == '<':
            marker -= 1
        elif code[i] == '*':
            tape[marker] = change[tape[marker]]  # use dict to swap 0 to 1 or 1 to 0
        elif code[i] == '[' and tape[marker] == '0':
            # call function iterator_position and find matching close bracket despite on amount of nested loops
            i = iterator_position(i, code, ']', '[') - 1
        elif code[i] == ']' and tape[marker] == '1':
            # use the same function, but we pass in input reverced string of code
            # as a result we get position of bracket in reverced string and we need to get index in normal string so use get len() - 1 - index
            i = len(code) - 1 - iterator_position(len(code) - i - 1, code[::-1], '[', ']')
        i += 1
    return ''.join(tape)


# This function increment counter value when element of string == brack 2
# and decrement when element of string ++ brack_1
# We start ro find only from i position

def iterator_position(i, code, brack_1, brack_2):
    brack_position = 0                              # simple counter
    for ind in range(len(code[i:])):
        if code[i:][ind] == brack_1:
            brack_position -= 1
            if brack_position == 0:
                return ind + len(code[:i])
        elif code[i:][ind] == brack_2:
            brack_position += 1
