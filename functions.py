import re
from tkinter.messagebox import *
key_word = {'if': 'IF',
            'then': 'Then',
            'else': 'ELSE',
            'end': 'END',
            'repeat': 'REPEAT',
            'until': 'UNTIL',
            'read': 'READ',
            'write': 'WRITE'}
special_symbol = {'+': 'PLUS',
                  '-': 'MINUS',
                  '*': 'ASTERISK',
                  '/':'DIVISION SLASH',
                  '=': 'EQUAL',
                  '<': 'STRICT INEQUALITY',
                  '(': 'LEFT BRACKET',
                  ')': 'RIGHT BRACKET',
                  ';': 'SEMI COLON',
                  ':=': 'ASSIGN'}
out = []
open_list = ["{", "(", "["]
close_list = ["}", ")", "]"]


def check(my_str):
    stack = []
    for i in my_str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i) # 2
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"


def get_token(code):
    lines = [line for line in code.split('\n') if line.strip() != '']
    for line in lines:
        line = line.strip()
        splited_line = list(line.split(" "))
        for word in splited_line:
            if word in key_word:
                out.append('  ' + word + '   => ' + key_word[word])
            elif word in special_symbol:
                out.append('  ' + word + '   => ' + special_symbol[word])
            elif re.match(r'\d+$', word):
                out.append('  ' + word + '   => NUM')
            elif re.match(r'\d;$', word):
                out.append('  ' + word[:-1] + '   => NUM')
                out.append('  ' + word[-1] + "   => SEMI COLON")
            elif re.match(r'^([a-zA-Z]+)$', word):
                out.append('  ' + word + '   => ID')
            elif re.match(r'^([a-zA-Z]+)(\[]*)', word):
                out.append('  ' + word[:word.index('[')] + '   => ID')
                out.append('  ' + word[word.index('[')+1:word.index(']')] + '   => INDEX')
            elif re.match(r'^([a-zA-Z]);$', word):
                out.append('  ' + word[:-1] + '   => ID')
                out.append('  ' + word[-1] + "   => SEMI COLON")
            elif re.match(r'\[[a-zA-Z]]', word):
                out.append('  ' + word[1:-2] + '   => ID')
            elif re.match(r'\(([a-zA-Z]+)\)', word):
                out.append('  ' + word[1:-1] + "   => CONDITION")
            elif re.match(r'{', word):
                break
            else:
                out.append('error')
    return out


def reform_input(file):
    f = open(file, "r")
    if f.mode == "r":
        in_ = f.read()
        in_ = re.sub(r'\s*{[^}]*}', '', in_)
        copying = True
        with open('pro.txt', 'rt') as inf, open('output_file.txt', 'wt') as outf:
            for line in inf:
                if copying:
                    if line.startswith('{'):
                        copying = False
                    else:
                        outf.write(line)
                elif line.endswith('}'):
                    copying = True
        if check(in_) == "Balanced":
            return get_token(in_)
        else:
            showerror("ERROR", "Your input Unbalanced brackets")
