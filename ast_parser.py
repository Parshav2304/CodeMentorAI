import ast

class CodeASTAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loops = 0
        self.functions = 0
        self.exceptions = 0
        self.recursion = False

    def visit_For(self, node):
        self.loops += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.loops += 1
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.functions += 1
        for n in ast.walk(node):
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
                if n.func.id == node.name:
                    self.recursion = True
        self.generic_visit(node)

    def visit_Try(self, node):
        self.exceptions += 1
        self.generic_visit(node)


def analyze_code(code: str):
    tree = ast.parse(code)
    analyzer = CodeASTAnalyzer()
    analyzer.visit(tree)
    return {
        "loops": analyzer.loops,
        "functions": analyzer.functions,
        "exceptions": analyzer.exceptions,
        "recursion": int(analyzer.recursion)
    }
