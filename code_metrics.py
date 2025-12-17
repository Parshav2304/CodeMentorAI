import ast

def cyclomatic_complexity(code):
    tree = ast.parse(code)
    complexity = 1

    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.For, ast.While, ast.And, ast.Or, ast.ExceptHandler)):
            complexity += 1
    return complexity


def nesting_depth(node, depth=0):
    if not hasattr(node, 'body'):
        return depth
    return max([nesting_depth(child, depth + 1) for child in node.body] + [depth])


def max_nesting(code):
    tree = ast.parse(code)
    return max(nesting_depth(tree), 0)
