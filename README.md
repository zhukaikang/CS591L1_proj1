# Readme file

## BNF Notation


    program = statement
         | statement program
         
    stmt = Assign(expr* targets, expr value)
      | Import(alias* names)
      | Expr(expr value)

    expr = Dict(expr* keys, expr* values)
       | Set(expr* elts)
       | List(expr* elts, expr_context ctx)
       | Call(expr func, expr* args, keyword* keywords)
       | Num(object n)
       | Str(string s)
       | Tuple(expr* elts, expr_context ctx)
       
## Methods I use
   I use python as the host language. This subset of language support 
auto checking language type, reading in different kinds of data consisting of DataFrame, 
statically analyzing the whole memory of DataFrame use. I assume that in this subset of language, 
all the read-in data structure would be inputted into DataFrame as an argument.

   For each cell in DataFrame, I assume it needs 8 bytes memory. 
I would count all the cells in the dataframe and ouput the final result.
I would write pandas as pd in the following formulas.
The operations I used in this project mainly include the following:
1. read data from a list(pd.DataFrame([])).
2. read data from a dict.
3. read data from a csv file.
4. read data from a tuple.
5. use pd.concat() to connect two DataFrame together.

## Algorithms
1. Auto check the program

    I rewrite the methods in class NodeVisitor to check the program. 
    This method would go through all of the ast to make sure the program only included import, data structure declaration and function call statement.
    And among function call, only methods in pd.DataFrame(), pd.read_csv(), pd.concat() are allowed.
2. Remove additional print statement using ast.NodeTransformer

    Since this subset of language doesn't support print() function. 
This method would rewrite methods in NodeTransformer to change the structure of ast. 
This function would be called before we auto check the language type.

3. Static analysis of the memory used by DataFrame
    
    I rewrite methods in the ast.NodeVisitor class to go through the ast. 
    When encounter number or string, the program would add 1 to the total memory.
    The program would finally output the total memory.
