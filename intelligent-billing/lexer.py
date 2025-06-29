import ply.lex as lex

# List of token names
tokens = [
    'ID', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUALS', 'PLUSEQUAL',
    'EQ', 'NE', 'GT', 'LT', 'GE', 'LE',
    'AND', 'OR', 'NOT',
    'LPAREN', 'RPAREN',
    'QUESTION', 'COLON',
    'BOOL'
]

# Regular expression rules for simple tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_EQUALS    = r'='
t_PLUSEQUAL = r'\+='
t_EQ        = r'=='
t_NE        = r'!='
t_GT        = r'>'
t_LT        = r'<'
t_GE        = r'>='
t_LE        = r'<='
t_AND       = r'&&'
t_OR        = r'\|\|'
t_NOT       = r'!'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_QUESTION  = r'\?'
t_COLON     = r':'

# Ignore whitespace
t_ignore = ' \t'

# Boolean values
def t_BOOL(t):
    r'true|false'
    t.value = True if t.value == 'true' else False
    return t

# Identifiers (e.g., variable names)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Numbers (integers and floats)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Newlines for line tracking
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

if __name__ == "__main__":
    data = "total = base + (units * rate) + (isPeak ? surcharge : 0);"
    lexer.input(data)
    for tok in lexer:
        print(tok)
