import ast
import inspect
from testcase import input_true, input_wrong
import pandas as pd
import astpretty
import astor

class auto_check(ast.NodeVisitor):

    #return true if find func.attr in [DataFrame(), concat(), read_csv()]
    def visit_Module(self, node):
        for s in node.body:
            if type(s) not in [ast.Import, ast.Assign, ast.Expr]:
                return False
            else:
                if not self.visit(s):
                    return False
        return True
        #
        # results = [self.visit(s) for s in node.body]
        # return all(results)

    def visit_Import(self, node):
        return True

    def visit_Assign(self, node):
        left = node.targets[0]
        if type(left) is not ast.Name:
            return False

        if left is None:
            return False

        right = node.value
        if type(right) not in [ast.Call, ast.List, ast.Dict, ast.Str, ast.Num, ast.Tuple]:
            return False
        return self.visit(node.value)

    def visit_Call(self, node):
        return self.visit(node.func)

    def visit_Tuple(self, node):
        for elt in node.elts:
            if type(elt) not in [ast.Str, ast.Num, ast.List, ast.Dict]:
                return False
        return True

    def visit_Dict(self, node):
        for key in node.keys:
            if type(key) not in [ast.Str, ast.Num, ast.List, ast.Dict]:
                return False

        for value in node.values:
            if type(value) not in [ast.Str, ast.Num, ast.List, ast.Dict]:
                return False
        return True

    def visit_List(self, node):
        if (len(node.elts) == 0):
            return True
        for n in node.elts:
            if type(n) not in [ast.Str, ast.Num, ast.List, ast.Dict]:
                return False
        return True

    def visit_Attribute(self, node):
        if node.attr in ['DataFrame', 'concat', 'read_csv']:
            return True
        else:
            return False

    # def visit_BinOp(self, node):
    #     return self.visit(node.left) and self.visit(node.right)
    #
    # def visit_Num(self, node):
    #     return True

class remove_print(ast.NodeTransformer):

    # def visit_Module(self, node):
    #     for s in node.body:
    #         if type(s) == ast.Expr:
    #             self.visit(s)

    def visit_Expr(self, node):
        ast.Pass()
    # def visit_Print(self, node):
    #     return ast.Pass()

parsed_str = ast.parse(input_true)
remove_print().visit(parsed_str)
#print(astor.to_source(parsed_str))
#print(astpretty.pprint(parsed_str))
# print(astpretty.pprint(parsed_num))
b_true = auto_check().visit(parsed_str)
print(b_true)

parsed_str = ast.parse(input_wrong)
remove_print().visit(parsed_str)
b_wrong = auto_check().visit(parsed_str)
print(b_wrong)
