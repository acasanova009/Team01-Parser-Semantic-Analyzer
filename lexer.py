import ply.lex as lex

# List of token names
tokens = (
    'INT',          # 'int' keyword
    'BOOL',
    'RETURN',       # 'return' keyword
    'TRUE',       # false
    'FALSE',       # true
    'IF',           # 'if' keyword for control structure
    'ELSE',         # 'then' keyword (if you need it)
    'PRINT',        # 'printf' function or print keyword
    'ID',           # Identifier (variable names)
    'NUMBER',       # Integer literals
    'PLUS',         # +
    'MINUS',        # -
    'TIMES',        # *
    'EXP',        # *
    'DIVIDE',       # /
    'OR',           # ||
    'AND',          # &&
    'EQ',           # ==
    'NEQ',           # !=
    'LE',           # <=
    'GE',           # >=
    'LT',           # < (Less Than)
    'GT',           # > (Greater Than)
    'EQUAL',        # =
    'LPAREN',       # (
    'RPAREN',       # )
    'LBRACE',       # {
    'RBRACE',       # }
    'COMMA',        # ,
    'SEMICOLON',    # ;
    'STRING',       # String literals
)

# Regular expression rules for simple tokens
t_EXP = r'\^'
t_TIMES = r'\*'
t_PLUS = r'\+'
t_MINUS = r'-'

t_OR = r'\|\|'           # Logical OR
t_AND = r'&&'            # Logical AND
t_EQ = r'=='             # Equality check
t_NEQ = r'!='            # Inequality check
t_LE = r'<='             # Less than or equal to
t_GE = r'>='             # Greater than or equal to
t_LT = r'<'              # Less than
t_GT = r'>'              # Greater than
t_EQUAL = r'='           # Assignment operator
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'

# Keywords
reserved = {
    'int': 'INT',
    'bool': 'BOOL',
    'True': 'TRUE',
    'False': 'FALSE',
    'return': 'RETURN',
    'if': 'IF',
    'else': 'ELSE',
    'printf': 'PRINT',
}

# A rule for identifiers (variable names)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t

# A rule for integer literals
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# A rule for string literals
def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # Remove the quotes
    return t

# Track line numbers
def t_newline(t):
    r'\n+'

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
