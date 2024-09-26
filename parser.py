import lexer
#NODES

class Number:
    
    def __init__(self, token) -> None:
        self.token = token
        
    def __repr__(self) -> str:
        return f'{self.token}'
    
class BinaryOp: 
    
    def __init__(self,left_node, token, right_node):
        self.left_node = left_node
        self.token = token
        self.right_node = right_node
        
    def __repr__(self) -> str:
        return f'({self.left_node}, {self.token}, {self.right_node})'
    
#PARSER

class Parser:
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_idx = -1
        self.advance()
        
    def advance(self):
        self.token_idx += 1
        if self.token_idx < len(self.tokens):
            self.current_token = self.tokens[self.token_idx]
        return self.current_token
    
    def factor(self):
        token = self.current_token
        if token.type in (lexer.INT, lexer.FLOAT):
            self.advance()
            return Number(token)
        
    def term(self):
        left_factor = self.factor()
        while self.current_token.type in (lexer.MUL, lexer.DIV):
            op = self.current_token
            self.advance()
            right_factor = self.factor()
            left_factor = BinaryOp(left_factor, op, right_factor)
        return left_factor
        
    def exp(self):
        left_term = self.term()
        while self.current_token.type in (lexer.PLUS, lexer.MINUS):
            op = self.current_token
            self.advance()
            right_term = self.term()
            left_term = BinaryOp(left_term, op, right_term)
        return left_term
    
    def parse(self):
        exp = self.exp()
        return exp