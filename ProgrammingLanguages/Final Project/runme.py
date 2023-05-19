import Nothyp, Interpreter
import traceback
import sys, os
from lark import Lark
from lark.lexer import Token
from lark.tree import Tree
from lark.exceptions import LarkError

g = Nothyp.grammar
parser = Lark(g)

while True:
    print("Insert Example (enter E to exit): ")
    try:
        s = input()
        if s == 'E':
            break
        tree = parser.parse(s)
        print("\nTree: \n", tree.pretty())
        print("Translated: \n", Interpreter.translate(tree), "\n")

    except LarkError as e:
        print("Error: ", e)

    except Exception as e:
        print("Error: ", traceback.format_exc())
        sys.exit(1)

