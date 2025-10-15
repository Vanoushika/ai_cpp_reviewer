![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.37.1-FF4B4B.svg)
![Transformers](https://img.shields.io/badge/Transformers-4.44.2-yellow.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Project-Completed-success.svg)

# 🤖 AI-Powered C++ Code Reviewer (Offline)
# 🤖 AI-Powered C++ Code Reviewer (Offline)

An **offline AI-driven static analysis tool** that scans C++ source files to detect unsafe functions, unused variables, and potential memory leaks — then generates **AI-based explanations and safer code suggestions** using lightweight Transformer models.

---

## 🧠 Project Overview

This project demonstrates how **AI and Natural Language Processing (NLP)** can be integrated with **static code analysis** to create an intelligent C++ code review assistant.  
It’s implemented in **Python + Streamlit** and uses **Hugging Face Transformers** for generating explanations and suggested fixes — all working locally (no cloud dependencies).

---

## 🏗️ Architecture

[User Uploads C++ File]
↓
[Parser]
↓
[Analyzer]
↓
[AI Explainer (LLM)]
↓
[Reporter + Streamlit UI]

Each module plays a specific role:
- **Parser** → Reads uploaded C++ files.
- **Analyzer** → Detects risky code patterns.
- **AI Explainer** → Uses a transformer model to explain & suggest fixes.
- **Reporter** → Exports structured JSON reports.
- **Dashboard (Streamlit)** → User-friendly offline web interface.

---

## ⚙️ Installation & Setup

### Prerequisites
- Python ≥ 3.10  
- Git  
- Virtual environment (recommended)

### Steps
```bash
# 1. Clone the repository
git clone https://github.com/Vanoushika/ai_cpp_reviewer.git
cd ai_cpp_reviewer

# 2. Create & activate virtual environment
python3 -m venv .venv
source .venv/bin/activate    # (Mac/Linux)
# .venv\Scripts\activate     # (Windows)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit dashboard
python -m streamlit run src/dashboard.py


🧩 Example Workflow

Upload a C++ source file (.cpp) in the Streamlit interface.

The analyzer scans for:

Unsafe functions (gets(), scanf(), etc.)

Unused variables

Potential memory leaks

The AI model provides explanations and suggested code fixes.

A structured JSON report is generated and can be downloaded.


Sample Output (JSON)

[
  {
    "type": "Potential Memory Leak",
    "pattern": "missing delete",
    "message": "Memory allocated but not freed properly.",
    "ai_explanation": "Missing delete[] may cause heap memory leaks."
  }
]


📦 Folder Structure

ai_cpp_reviewer/
├── src/
│   ├── parser.py
│   ├── analyzer.py
│   ├── ai_explainer.py
│   ├── reporter.py
│   └── dashboard.py
├── reports/
│   └── dashboard_result.json
├── .venv/
├── requirements.txt
└── README.md


📈 Results

| File         | Issue Detected        | AI Explanation          | Suggested Fix                     |
| ------------ | --------------------- | ----------------------- | --------------------------------- |
| `leak.cpp`   | Potential Memory Leak | Missing delete[]        | Adds `delete[] arr;`              |
| `unsafe.cpp` | Unsafe Function       | gets() unsafe           | Use `fgets()` or `std::getline()` |
| `unused.cpp` | Unused Variable       | Declared but never used | Remove or utilize the variable    |


🚀 Future Enhancements

Support for Python and Java static analysis.

Fine-tuned LLM for context-aware fix suggestions.

Batch analysis for multiple files.

Offline caching for faster Transformer inference.


🧑‍💻 Contributors
Anoushika Vennamaneni


📜 License
This project is released under the MIT License.
You are free to use, modify, and distribute it with attribution.
