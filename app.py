import streamlit as st

from analyzer.ast_parser import analyze_code
from analyzer.code_metrics import cyclomatic_complexity, max_nesting
from recommender.task_generator import generate_task

st.title("CodeMentorAI – Python Code Weakness Analyzer")

code = st.text_area("Paste your Python code here")

if st.button("Analyze"):
    if not code.strip():
        st.warning("Please paste some Python code.")
    else:
        ast_data = analyze_code(code)

        metrics = {
            "complexity": cyclomatic_complexity(code),
            "nesting": max_nesting(code)
        }

        result = {
            "analysis": ast_data,
            "metrics": metrics,
            "recommendation": generate_task(0)
        }

        st.subheader("Analysis Result")
        st.json(result)
