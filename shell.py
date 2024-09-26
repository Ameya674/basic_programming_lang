from lexer import Lexer
from parser import Parser

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error: return error, None
    parser = Parser(tokens)
    ast = parser.parse()
    return ast, None


while True:
    text = input("basic > ")
    result, error = run("<stdin>", text)
    if error: print(error.error_printing())
    else: print(result)