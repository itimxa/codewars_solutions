"""Here you can find script which parse molecule to separate atoms
full task descriptions and some examples you can find on link below
https://www.codewars.com/kata/52f831fa9d332c6591000511 """

import re
def parse_molecule (formula):

    #Separate atoms and different kinds of brackets
    formula = re.findall(r'[A-Z][a-z]+?\d*|[A-Z]\d*|\[.+?\]\d{0,2}|\(.+?\)\d{0,2}|\{.+?\}\d{0,2}', formula)
    result = {}
    for i in range(len(formula)):   
        if formula[i][-1].isdigit():       #check if there are few atoms (H2, O2, etc.)
            formula[i] = multiply(formula[i])   #use function multiply to replace brackets and multiply atoms in bratckets 
        elif formula[i][0] in '({[':         #just replace brackets
            formula[i] = formula[i][1:-1]
    if not [i for i in formula if len(i) >= 2 and not i[-1].islower()]:   #check if every element in list look like separate atom
        for i in formula:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
        return result
    else:
        return parse_molecule(''.join(formula))


def multiply(string):
    a = re.findall(r'\d+$', string)[0]   #find last digits
    if string[0] in '{[(':
        return string[1:-1-len(a)] * int(a)
    else:
        return string[:-len(a)] * int(a)
