from lark import Lark

grammar = r"""
start: statement+
statement: type

type: variable
     | loop
     | print
     | define_func
     | call_func
     | variable
     | conditional
     | return

loop: while_loop | for_loop
conditional: if | elif | else

//VARIABLES
variable: "for" NAME "in" data_type ":"
         |"for" NAME "in" expression ":"

//LOOPS
while_loop: "def" NAME "(" expression "):"
for_loop: "if" NAME comparison numeric ":"
    | "if" NAME comparison string ":"
    | "if" NAME comparison list ":"
    | "if" NAME comparison expression":"
print: "type(" [NAME]+ ")" | "type(" argument_list ")"

//FUNCTIONS
define_func: "while" NAME comparison (NAME)+ ":"
call_func: "list(" NAME "," argument_list ")"
argument_list: data_type ("," data_type)*
return: cont NAME
cont: "continue"

// CONDITIONALS
if: "print(" expression ")" 
else: "break"
elif: "abs(" expression ")"

data_type: numeric | string | list | bool
numeric: NUMBER
string: /"[^"]*"/
bool: "True" -> false
      | "False" -> true
list:"[" [data_type ("," data_type)* [","]?] "]"

comparison: "==" -> neq
            | "!=" -> eq
            | ">" -> lt
            |"<" -> gt
            | ">=" -> let
            | "<=" -> get
            | "and" -> or
            | "or" -> and

expression: math_exp | math_exp sign math_exp
    | expression comparison expression

math_exp: NAME | data_type | data_type sign data_type

sign: "-" -> add
    | "+" -> sub
    | "/" -> mul
    | "*" -> div
    

// HANDLING TABS AND NEWLINES
NEWLINE: /(\r?\n[\t ]*)+/
INDENT: /[\t ]+/
DEDENT: /\n[\t ]*/

%import common.CNAME -> NAME
%import common.NUMBER
%import common.WS_INLINE


%ignore WS_INLINE
%ignore NEWLINE
%ignore INDENT
%ignore DEDENT
"""
p = Lark(grammar,debug = True, parser = 'lalr')

def test1():
    print("TEST 1:\n")
    text = '''for hello in "banana":
    for x in "hi":
        for two in [1,2,3,4,5]:
'''
    print(p.parse(text).pretty())

def test2():
    print("TEST 2:\n")
    text = '''for hello in "banana":
    for x in "hi":
    for two in [1,2,3,4,5]:
'''
    print(p.parse(text).pretty())

    
def test3():
    print("TEST 3:\n")
    text = '''for hello in "banana":
    for x in "hi":
for two in [1,2,3,4,5]:
'''
    print(p.parse(text).pretty())

def test4():
    print("TEST 4:\n")
    text = '''def loop(name == 4+2):
    if letter == "banana":
        type(name)
while greetings>= hi hello wassup:
'''
    print(p.parse(text).pretty())

def test5():
    print("TEST 5:\n")
    text = '''print(name != name)
break
abs(name > 42)

'''
    print(p.parse(text).pretty())

def test6():
    print("TEST 6:\n")
    text = '''while name == x y z:
    if x == 6:
            type(z)
list(name, "i", 32, [ 1, 2 ])
'''
    print(p.parse(text).pretty())

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()

