import ply.yacc as yacc
from lexer import tokens
import math

symbol_table = {}

# Tabla de símbolos inicializada como un diccionario vacío
symbol_table = {}


errorSemantic = 0
# Función para declarar una variable en la tabla de símbolos
def declare_variable(name, var_type, value):
    """
    Declara una nueva variable en la tabla de símbolos.
    Verifica si el nombre de la variable ya existe y, si no, lo agrega.
    """
    # Print the current symbol table for debugging
    #print(f"ANTES nueva var: :  <ID = expression>")

    #print(symbol_table)
    #print(f"-----------------")
    # Check if the variable is already declared
    if name in symbol_table:
        print(f"Error: The variable '{name}' is already declared.")
        return False  # Variable already declared

    # Add the variable with the specified type and value if type compatibility is met
    if (var_type == "int" and isinstance(value, int) and not isinstance(value, bool)) or \
       (var_type == "bool" and isinstance(value, bool)):
        symbol_table[name] = {'type': var_type, 'value': value}
        return True  # Variable successfully added
    
    # Type incompatibility error
    print(f"Error: Type mismatch for variable '{name}'. Expected {var_type}, got {type(value).__name__}.")
    return False  # Type incompatibility


# Función para asignar un valor a una variable existente en la tabla de símbolos
def assign_variable(name, value):
    """
    Asigna un valor a una variable existente en la tabla de símbolos.
    Verifica si el tipo de dato coincide con el tipo declarado de la variable.
    """

     # Print the current symbol table for debugging
    #print(f"ANTES asignar: :  <ID = expression>")

    #print(symbol_table)
    #print(f"-----------------")

    if name in symbol_table:
        # Verifica si el tipo del valor coincide con el tipo declarado
        var_type = symbol_table[name]['type']
        if (var_type == "int" and isinstance(value, int) and not isinstance(value, bool))or \
           (var_type == "bool" and isinstance(value, bool)):
            # Asigna el valor si el tipo es compatible
            symbol_table[name]['value'] = value

            #print(f"DESPUES asignar: :  <ID = expression>")
            
            #print(symbol_table)
            #print(f"-----------------")

            return True  # Asignación exitosa
               
        else:
            errorSemantic = 1
            print(f"Error: Tipo de dato incompatible para la variable '{name}'.")
            return False  # Error de tipo de dato
    else:
        print(f"Error: The variable '{name}' has not been declared.")
        return False  # La variable no existe


     
    # Print the current symbol table for debugging
    #print(f"Tabla de simbolos :")

    #print(symbol_table)
    #print(f"-----------------")

def get_variable_value(name):
    """
    Retorna el valor de la variable si está declarada en la tabla de símbolos.
    Si la variable no existe, muestra un mensaje de error.
    """
    if name in symbol_table:
        #print(f"The variable was read properly")
        return symbol_table[name]['value']
    else:
        print(f"Error: The variable '{name}' has not been declared.")
        return None



#---------------------------------SEMATICOS------------


def check_int_operands(op1, op2):
    """
    Verifica que ambos operandos sean del tipo `int` para operaciones aritméticas.
    Retorna True si ambos son `int`, False si no.
    """
    if isinstance(op1, int) and not isinstance(op1, bool) and \
       isinstance(op2, int) and not isinstance(op2, bool):
        return True
    else:
        print("Semantic error: Arithmetic operation requires integer types.")
        errorSemantic = 1
        return False
    

def check_bool_operands(op1, op2):
    """
    Verifica que ambos operandos sean del tipo `bool` para operaciones lógicas.
    Retorna True si ambos son `bool`, False si no.
    """
    
    if isinstance(op1, bool) and isinstance(op2, bool) :
        return True
    else:
        print("Error: Operación lógica requiere operandos de tipo bool.")
        errorSemantic = 1
        return False


#-----------------------------------


def p_program_function(p):
    'program : function'
    p[0] = p[1]



def p_function(p):
    'function : INT ID LPAREN RPAREN LBRACE block RETURN  NUMBER SEMICOLON RBRACE'
    p[0] = ('Function\n',p[1],p[2],p[3],p[4], p[5],p[6],p[7],p[8],p[9],p[10] )

def p_block(p):
    '''block : block statement'''
    
    p[0] = ('Block',p[1] ,p[2])

def p_block_empty(p):
    '''block : empty'''
    p[0] = ('Block',p[1])


# int a = 15;
def p_statement_variable(p):
    '''statement : INT ID EQUAL expression SEMICOLON'''

    # Check if the expression is of type int
    
    if (isinstance(p[4], int)):
        # Declare the variable with type "int"
        if declare_variable(p[2], "int", p[4]):
            # Store the variable information in the parse tree node
            #print('New variable', "int", p[2], p[3], p[4], p[5])
            p[0] = p[4]
        
    else:
        errorSemantic = 1
        print("Semantic error. Trying to assing different type to INT variable.", p[2])


    
        
    # Print the current symbol table for debugging
    #print(f"Tabla de simbolos :  <int id=expression>")

    #print(symbol_table)
    #print(f"-----------------")



def p_statement_variable_bool(p):
    '''statement : BOOL ID EQUAL expression SEMICOLON'''
    
     # Check if the expression is of type int
    
    if (isinstance(p[4], bool)):
        # Declare the variable with type "int"
        if declare_variable(p[2], "bool",p[4] ):
            # Store the variable information in the parse tree node
            #print('variable', "bool", p[2], p[3], p[4], p[5])
            p[0] = p[4]
        
    else:
        errorSemantic = 1
        print("Semantic error. Trying to assing different type to BOOL variable.", p[2])


    
        
    # Print the current symbol table for debugging
    #print(f"Tabla de simbolos :  <int id=expression>")

    #print(symbol_table)
    #print(f"-----------------")



def p_statement_assignment(p):
    '''statement : ID EQUAL expression SEMICOLON'''

    
    if assign_variable(p[1], p[3]):
        p[0]=p[3]
    else:
        errorSemantic = 1
        print("Semantic error. Incompatible Assignment")

    
#SI Alguien quiere agregar el if else, que sea feliz.
#def p_statement_if_else(p):
    #'''statement : IF LPAREN expression RPAREN LBRACE statement RBRACE ELSE  LBRACE statement RBRACE'''
    #print('IF (',p[3],'){', p[6], '}else {', p[10],'}' )

    #if (p[3]):
    #    p[0] = ('IF (',p[3],'){', p[6], '}else {', p[10],'}' )
    #else:
    #p[0] = ('IF (',p[3],'){', p[6], '}else {', p[10],'}' )

#statement
#block
def p_statement_if(p):

    '''statement : IF LPAREN logical_a RPAREN LBRACE block RBRACE '''
    #print('Resultado logico del "if"', p[3])

    if(p[3]):
        p[0] = p[6]
    
    

# Grammar rules with AST construction
#------------------------------------------------------------------------------------------
# Logical OR expression -------------------------------------------------BOOLS
# Logical OR expression
def p_logical_or(p):
    'logical_a : logical_a OR logical_b'
    if (check_bool_operands(p[1] ,p[3])):
        p[0] = (p[1] or p[3])
    else:
        errorSemantic = 1
        print("Semantic error in OR operator")

def p_logical_or_direct(p):
    'logical_a : logical_b'
    p[0] = p[1]

# Logical AND expression
def p_logical_and(p):
    'logical_b : logical_b AND logical_c'
   

    if (check_bool_operands(p[1] ,p[3])):
        p[0] = (p[1] and p[3])
    else:
        errorSemantic = 1
        print("Semantic error in AND operator")

def p_logical_and_direct(p):
    'logical_b : logical_c'  # Corrected from logical_b : logical_b
    p[0] = p[1]


# ---------------------------------------------------RELACIONALES (bool == bool y int == int)
# Equality comparator (==)
def p_comparator_equality(p):
    'logical_c : logical_c EQ logical_d'
    p[0] = (p[1] == p[3])

def p_comparator_equality_direct(p):
    'logical_c : logical_d'
    p[0] = p[1]
# ---------------------------------------------------RELACIONALES (sin bool)
# Relational operator <=
def p_relational_less_equal(p):
    'logical_d : logical_d LE expression'
   

    if (check_int_operands(p[1] ,p[3])):
        p[0] = (p[1] <= p[3])
    else:
        errorSemantic = 1
        print("Semantic error in <= operator")

# Relational operator >=
def p_relational_greater_equal(p):
    'logical_d : logical_d GE expression'
    
    
    if (check_int_operands(p[1] ,p[3])):
        p[0] = (p[1] >= p[3])
    else:
        errorSemantic = 1
        print("Semantic error in >= operator")

# Relational operator <
def p_relational_less(p):
    'logical_d : logical_d LT expression'
    

    if (check_int_operands(p[1] ,p[3])):
        p[0] = (p[1] < p[3])
    else:
        errorSemantic = 1
        print("Semantic error in < operator")

# Relational operator >
def p_relational_greater(p):
    'logical_d : logical_d GT expression'

    
    if (check_int_operands(p[1] ,p[3])):
        p[0] = (p[1] > p[3])
    else:
        errorSemantic = 1
        print("Semantic error in > operator")


# Fallback case for simple expression without relational/comparator operations
def p_relational_simple_direct(p):
    'logical_d : expression'
    p[0] = p[1]


#---------------------------------------------------------------------------------
def p_expression_plus(p):
    'expression : expression PLUS term'
    if (check_int_operands(p[1] ,p[3])):
        p[0] = p[1] + p[3]
    else:
        errorSemantic = 1
        print("Semantic error in + operand")



def p_expression_minus(p):
    'expression : expression MINUS term'
    if (check_int_operands(p[1] ,p[3])):
        p[0] = p[1] - p[3]
    else:
        errorSemantic = 1
        print("Semantic error in - operand")


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'

    
    if (check_int_operands(p[1] ,p[3])):
        p[0] = p[1] * p[3]
    else:
        errorSemantic = 1
        print("Semantic error in * operand")

def p_term_exponential(p):
    'term : factor'
    p[0] = p[1]

#Se puede agregar exponencial, cambiando arriba donde dice factor a exponential
#def p_exponential_factor(p):
 #   'exponential : exponential EXP factor'
  #  p[0] = p[1] ** p[3]

#def p_exponential_direct(p):
    #'exponential : factor'
    #p[0] = p[1]


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_true(p):
    'factor : TRUE'
    p[0] = True


def p_factor_false(p):
    'factor : FALSE'
    p[0] = False

#Verifica la existencia de una variable en la symbol table.
def p_factor_variable(p):
    'factor : ID'
    p[0] = get_variable_value(p[1])



def p_factor_expr(p):
    'factor : LPAREN logical_a RPAREN'
    p[0] = p[2]

def p_empty(p):
    'empty :'
    pass


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

data = '''
int main() {
    
    int a= 1;
    int b= 2;
    bool c = True;

    if (a<b || True)
    {
        b=b*8;
    }
    
    return 0;
}
'''


result = parser.parse(data)



if errorSemantic == 1:
    print("Semantic error in input!")


print("---Result---")
print(symbol_table)
print("------------")