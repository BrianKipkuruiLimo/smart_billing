import ply.yacc as yacc
from lexer import tokens  # Import tokens from lexer
from evaluator import variables

# Grammar rules

# Start rule
def p_statement_assign(p):
    'statement : ID EQUALS expression'
    p[0] = ('assign', p[1], p[3])

def p_statement_add_assign(p):
    'statement : ID PLUSEQUAL expression'
    p[0] = ('add_assign', p[1], p[3])

def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]

# Expression rules
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression GT expression
                  | expression LT expression
                  | expression GE expression
                  | expression LE expression
                  | expression EQ expression
                  | expression NE expression
                  | expression AND expression
                  | expression OR expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_ternary(p):
    'expression : expression QUESTION expression COLON expression'
    p[0] = ('if', p[1], p[3], p[5])

def p_expression_not(p):
    'expression : NOT expression'
    p[0] = ('not', p[2])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_bool(p):
    'expression : BOOL'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]

def p_expression_function(p):
    'expression : ID LPAREN expression RPAREN'
    p[0] = ('func', p[1], p[3])

# Error rule
def p_error(p):
    print("Syntax error at:", p.value if p else "EOF")

# Build the parser
parser = yacc.yacc()

# Optional REPL mode
if __name__ == "__main__":
    from evaluator import evaluate
    from visualizer import print_tree

    while True:
        try:
            s = input("expr > ")
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print("Expression Tree:")
        print_tree(result)
        try:
            output = evaluate(result)
            print("Result:", output)
            print("Variables:", variables)
        except Exception as e:
            print("Error:", e)
