import pandas as pd

def build_features(ast_data, metrics):
    features = {
        "loops": ast_data["loops"],
        "functions": ast_data["functions"],
        "exceptions": ast_data["exceptions"],
        "recursion": ast_data["recursion"],
        "complexity": metrics["complexity"],
        "nesting": metrics["nesting"]
    }
    return pd.DataFrame([features])
