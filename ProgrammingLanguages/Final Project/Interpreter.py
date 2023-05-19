import Nothyp
from lark import Lark
from lark.tree import Tree
from lark.indenter import Indenter
from lark.lexer import Token
grammar = Nothyp.grammar

def translate(node):
    if isinstance(node, Tree):
        if node.data != None:
            if node.data == "start":
                return "\n".join([translate(child) for child in node.children if child is not None])
            elif node.data == "statement":
                return translate(node.children[0])
            elif node.data == "type":
                return translate(node.children[0])
            elif node.data == "loop":
                return translate(node.children[0])
            elif node.data == "conditional":
                return translate(node.children[0])
            elif node.data == "variable":
                return f"{node.children[0]} = {translate(node.children[1]) if node.children[1] is not None else ''}"
            elif node.data == "while_loop":
                return f"while {translate(node.children[1]) if node.children[1] is not None else ''}:"
            elif node.data == "for_loop":
                return f"for {translate(node.children[0]) if node.children[0] is not None else ''} in {translate(node.children[2]) if node.children[2] is not None else ''}:"
            elif node.data == "print":
                args = ", ".join([translate(child) if child is not None else '' for child in node.children])
                return f"print({args})"

            #FUNCTIONS
            elif node.data == "define_func":
                args = ", ".join([translate(child) if child is not None else '' for child in node.children[2:]])
                return f"def {node.children[0]}({args}):"
            elif node.data == "call_func":
                args = ", ".join([translate(child) if child is not None else '' for child in node.children[1:]])
                return f"{node.children[0]}({args})"
            elif node.data == "argument_list":
                param = []
                for child in node.children:
                   param.append(translate(child))
                stringParam = ", ".join(param)
                return stringParam
            elif node.data == "return":
                return f"{translate(node.children[0])} {translate(node.children[1])}"
            elif node.data == "cont":
                return "return"

            #IF,ELSE,ELIF
            elif node.data == "if":
                return f"if {translate(node.children[0]) if node.children[0] is not None else ''}:"
            elif node.data == "elif":
                return f"elif {translate(node.children[0]) if node.children[0] is not None else ''}:"
            elif node.data == "else":
                return "else:"

            #DATATYPES
            elif node.data == "list":
                items = [translate(child) for child in node.children if child is not None]
                return f"[{', '.join(items)}]"
            elif node.data == "string":
                return node.children[0]
            elif node.data == "numeric":
                return node.children[0]
            elif node.data == "data_type":
                return translate(node.children[0])

            #BOOLEANS
            elif node.data == "bool":
                return node.children[0]
            elif node.data == "true":
                return "True"
            elif node.data == "false":
                return "False"

            #COMPARISONS
            elif node.data == "comparison":
                return node.children[0]
            elif node.data == "eq":
                return "=="
            elif node.data == "neq":
                return "!="
            elif node.data == "gt":
                return ">"
            elif node.data == "lt":
                return "<"
            elif node.data == "get":
                return ">="
            elif node.data == "let":
                return "<="
            elif node.data == "and":
                return "and"
            elif node.data == "or":
                return "or"

            #EXPRESSIONS
            elif node.data == "expression":
                if len(node.children) == 1:
                    return translate(node.children[0])
                else:
                    return f"{translate(node.children[0])} {translate(node.children[1])} {translate(node.children[2])}"
            elif node.data == "math_exp":
                if len(node.children) == 1:
                    return translate(node.children[0])
                else:
                    return f"{translate(node.children[0])} {translate(node.children[1])} {translate(node.children[2])}"
            elif node.data == "add":
                return "+"
            elif node.data == "sub":
                return "-"
            elif node.data == "mul":
                return "*"
            elif node.data == "div":
                return "/"
    elif isinstance(node, Token):
        if node.value != None:
            return node.value


parser = Lark(grammar)

def test1():
    print("TEST 1:\n")
    text = '''for hello in "banana":'''
    
    tree = parser.parse(text)
    translated = translate(tree)
    print("Translated: \n", translated, "\n")

def test2():
    print("TEST 2:\n")
    text = '''for hello in "banana":
    for x in "hi":
for two in [1,"test",[1,"hi"],"hello",True,False]:
'''

    tree = parser.parse(text)
    translated = translate(tree)
    print("Translated: \n", translated, "\n")

def test3():
    print("TEST 3:\n")
    text = '''for x in 7:
print(x == 9)
continue x
abs(x >= 9)
for i in 12+1:
continue i
break
for j in 24:
continue j
'''
    
    tree = parser.parse(text)
    translated = translate(tree)
    print("Translated: \n", translated, "\n")


def test4():
    print("TEST 4:\n")
    text = '''for x in 9:
    def  foo(x == 9):
    if letter == "banana":
        type(letter)
while x >= hi hello goodbye:
'''
    tree = parser.parse(text)
    translated = translate(tree)
    print("Translated: \n", translated, "\n")

def test5():
    print("TEST 5:\n")
    text = '''print(name != name)
break
abs(name > 42)

'''
    tree = parser.parse(text)
    translated = translate(tree)
    print("Translated: \n", translated, "\n")

def test6():
    print("TEST 6:\n")
    text = '''while fun == x y z:
    if q == y:
    type(x q z)
    list(fun, "there is a" , [1, 2 , 3 ,4 ,5], "in the list")
'''
    tree = parser.parse(text)
    translated = translate(tree)
    print("Translated: \n", translated, "/n")

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
