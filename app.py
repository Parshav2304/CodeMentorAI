import streamlit as st
import ast
import sys
import io

from ast_parser import analyze_code
from code_metrics import cyclomatic_complexity, max_nesting
from task_generator import generate_task

st.set_page_config(layout="wide")
st.title("CodeMentorAI – Intelligent Python Code Analyzer")

# -------------------------------
# Helper: Estimate Space Complexity
# -------------------------------
def estimate_space_complexity(code):
    tree = ast.parse(code)
    variables = 0
    lists = 0
    dicts = 0
    recursion = False

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            variables += 1
        elif isinstance(node, ast.List):
            lists += 1
        elif isinstance(node, ast.Dict):
            dicts += 1
        elif isinstance(node, ast.FunctionDef):
            for n in ast.walk(node):
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
                    if n.func.id == node.name:
                        recursion = True

    if recursion:
        return "O(n) (due to recursion stack)"

    if lists + dicts > 2:
        return "O(n) (dynamic data structures used)"

    return "O(1) (mostly constant space)"


# -------------------------------
# Layout: 3 Columns
# -------------------------------
col1, col2, col3 = st.columns(3)

# ===============================
# COLUMN 1 – CODE INPUT
# ===============================
with col1:
    st.subheader("📝 Paste Python Code")
    code = st.text_area(
        "User Code",
        height=400,
        placeholder="Paste your Python code here..."
    )

# ===============================
# COLUMN 2 – CODE EXECUTION
# ===============================
with col2:
    st.subheader("▶️ Code Execution Output")

    if st.button("Run Code"):
        if not code.strip():
            st.warning("Please paste Python code first.")
        else:
            try:
                old_stdout = sys.stdout
                sys.stdout = buffer = io.StringIO()

                # ⚠️ Restricted execution
                exec(code, {"__builtins__": {"print": print, "range": range}})

                sys.stdout = old_stdout
                output = buffer.getvalue()

                st.success("Execution Successful")
                st.code(output if output else "No output")

            except Exception as e:
                sys.stdout = old_stdout
                st.error("Runtime Error")
                st.code(str(e))

# ===============================
# COLUMN 3 – ANALYSIS & INSIGHTS
# ===============================
with col3:
    st.subheader("📊 Code Analysis & Insights")

    if code.strip():
        try:
            ast_data = analyze_code(code)

            metrics = {
                "Cyclomatic Complexity": cyclomatic_complexity(code),
                "Nesting Depth": max_nesting(code),
                "Space Complexity": estimate_space_complexity(code)
            }

            st.markdown("### 🔍 Structural Analysis")
            st.json(ast_data)

            st.markdown("### 📐 Metrics")
            st.json(metrics)

            st.markdown("### 🧠 Recommendation")
            st.info(generate_task(0))

            st.markdown("### 🧾 Reformatted Code View")
            st.code(code, language="python")

        except Exception as e:
            st.error("Analysis Error")
            st.code(str(e))
