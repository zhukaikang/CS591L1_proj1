import ast
import inspect
import os
from testcase import input_true, input_wrong

memory_each_cell = 8

class calculate_memory(ast.NodeVisitor):
    #assume each cell consumes 8 bytes
    memory = 0;
    def visit_Module(self, node):
        for s in node.body:
            if type(s) == ast.Assign:
                self.visit(s)
        return self.memory
        #
        # results = [self.visit(s) for s in node.body]
        # return all(results)

    # def visit_Import(self, node):
    #     return True

    def visit_Assign(self, node):
        if type(node.value) in [ast.Call, ast.List, ast.Dict, ast.Str, ast.Tuple]:
            self.memory += self.visit(node.value)

    def visit_Call(self, node):
        if node.func.attr == 'read_csv':
            return os.path.getsize(node.args[0].s)
        else:
            return 0

    def visit_Tuple(self, node):
        sum = 0
        for elt in node.elts:
            if type(elt) in [ast.Str, ast.Num, ast.List, ast.Dict]:
                sum += self.visit(elt)
        return sum

    def visit_Dict(self, node):
        sum = 0
        for key in node.keys:
            if type(key) in [ast.Str, ast.Num, ast.List, ast.Dict]:
                sum += self.visit(key)

        for value in node.values:
            if type(value) in [ast.Str, ast.Num, ast.List, ast.Dict]:
                sum += self.visit(value)
        return sum


    def visit_List(self, node):
        sum = 0
        for elt in node.elts:
            if type(elt) in [ast.Str, ast.Num, ast.List, ast.Dict]:
                sum += self.visit(elt)
        return sum

    def visit_Num(self, node):
        return 1

    def visit_Str(self, node):
        return 1


    def visit_Attribute(self, node):

        if node.attr == 'read_csv':
            os.path.getsize("test.csv")


parsed_str_true = ast.parse(input_true)

total_cell = calculate_memory().visit(parsed_str_true)
total_memory = total_cell * memory_each_cell
print(total_cell)
print('Total memory is: ', total_memory,'bytes')