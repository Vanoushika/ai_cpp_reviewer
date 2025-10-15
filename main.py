from src.parser import load_cpp_code
from src.analyzer import detect_issues
from src.reporter import print_console_report, save_json_report
from src.ai_explainer import add_ai_explanations

if __name__ == "__main__":
    code = load_cpp_code("tests/sample_code/test1.cpp")
    report = detect_issues(code)
    report = add_ai_explanations(report)
    print_console_report(report)
    save_json_report(report)
