from fastapi import FastAPI
from analyzer.ast_parser import analyze_code
from analyzer.code_metrics import cyclomatic_complexity, max_nesting
from ml.feature_builder import build_features
from recommender.task_generator import generate_task

app = FastAPI()

@app.post("/analyze")
def analyze(code: str):
    ast_data = analyze_code(code)
    metrics = {
        "complexity": cyclomatic_complexity(code),
        "nesting": max_nesting(code)
    }
    features = build_features(ast_data, metrics)
    return {
        "analysis": ast_data,
        "metrics": metrics,
        "recommendation": generate_task(0)
    }
