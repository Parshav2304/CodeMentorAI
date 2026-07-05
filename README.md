# 🤖 CodeMentorAI - Intelligent Programming Assistant & Code Analyzer

**CodeMentorAI** is an AI-powered static code analysis and adaptive learning platform. By parsing Abstract Syntax Trees (AST), evaluating complexity metrics, detecting code smells, and using machine learning to cluster user coding weaknesses, CodeMentorAI generates personalized coding tasks to help developers systematically improve their programming skills.

---

## 📐 System Pipeline

```
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│  Source Code    │ ────> │   AST Parser    │ ────> │ Smell Detector  │
│  (User Input)   │       │ (ast_parser.py) │       │(smell_detector) │
└─────────────────┘       └─────────────────┘       └────────┬────────┘
                                                             │
                                                             ▼
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ Custom Coding   │ <──── │ Task Generator  │ <──── │  ML Weakness    │
│ Exercises Output│       │(task_generator) │       │   Clustering    │
└─────────────────┘       └─────────────────┘       └─────────────────┘
```

---

## ✨ Features & Architecture

- **AST Parsing (`ast_parser.py`)**: Evaluates the lexical structure of Python code, extracting class declarations, function signatures, loop depths, and control flow nodes.
- **Metrics Computation (`code_metrics.py`)**: Measures cyclomatic complexity, logical lines of code, and inheritance nesting depth.
- **Code Smell Detection (`smell_detector.py`)**: Scans codebases for common architectural anti-patterns, including:
  - Long Method (excessive statement count)
  - God Class (too many fields and methods)
  - Deep Nesting (excessive conditional branch layering)
- **Unsupervised Weakness Clustering (`weakness_clustering.py`)**: Utilizes K-Means clustering (from `scikit-learn`) on historical user telemetry to identify distinct categories of coding mistakes or conceptual gaps.
- **Adaptive Task Generator (`task_generator.py`)**: Programmatically creates targeted programming challenges to address specific weak clusters identified by the ML engine.
- **Skill Tracking (`skill_tracker.py`)**: Records a history of analyzed metrics and dynamically updates the developer's proficiency logs.

---

## 🛠️ Tech Stack & Libraries

- **Python 3.10+**
- **AST** - Native Python Abstract Syntax Trees library.
- **Scikit-learn** - K-Means clustering for categorizing coding errors.
- **Pandas & NumPy** - Parsing and formatting user code metrics.
- **FastAPI / Flask** - API server framework.

---

## 🚀 Getting Started

### 1. Installation
Clone the repository:
```bash
git clone https://github.com/Parshav2304/CodeMentorAI.git
cd CodeMentorAI
```

### 2. Set Up Environment
Create a virtual environment and install requirements:
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Running the Analyzer
Analyze a script directly from the command line:
```bash
python main.py --file path/to/your_code.py
```

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.