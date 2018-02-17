"""Realization of Paintfuck interpreter on Python
Link to task description you can find below
https://www.codewars.com/kata/5868a68ba44cfc763e00008d"""

def interpreter(code, iterations, width, height):
    draw_field = [[0]*width for i in range(height)]
    r_ind = c_ind = i = j = 0
    widt_d = {-1: width-1, width: 0}
    height_d = {-1: height-1, height: 0}
    while j != iterations:
        if r_ind == -1 or r_ind == height:    # if/else statement to prevent 'list index out of range'
            r_ind = height_d[r_ind]           # we use dictionary to provide toroidal behaviour
        elif c_ind == -1 or c_ind == width:
            c_ind = widt_d[c_ind]
        if i == len(code):
            break
        if code[i] == 'n':
            r_ind -= 1
        elif code[i] == 'e':
            c_ind += 1
        elif code[i] == 's':
            r_ind += 1
        elif code[i] == 'w':
            c_ind -= 1
        elif code[i] == '*':
            draw_field[r_ind][c_ind] = 1 - draw_field[r_ind][c_ind]
        elif code[i] == '[' and draw_field[r_ind][c_ind] == 0:
            # call function iterator_position and find matching close bracket despite on amount of nested loops
            i = brack_position(code, i, '[', ']')              
        elif code[i] == ']' and draw_field[r_ind][c_ind] == 1:
            # use the same function, but we pass in input reverced string of code
            # as a result we get position of bracket in reverced string
            # we need to get index in normal string so use get len() - 1 - index
            i = len(code) - 1 - brack_position(code[::-1], len(code) - 1 - i, ']', '[')
        elif code[i] not in 'news*[]':  # ignore invalid commands
            j -= 1
        j += 1
        i += 1
    return '\r\n'.join(''.join(str(k) for k in string) for string in draw_field)


def brack_position(code, i, start_brack, need_brack):
    brack_ind = 0  # simple counter
    for ind in range(len(code[i:])):
        if code[i:][ind] == need_brack:
            brack_ind -= 1
            if brack_ind == 0:
                return ind + len(code[:i])
        elif code[i:][ind] == start_brack:
            brack_ind += 1
