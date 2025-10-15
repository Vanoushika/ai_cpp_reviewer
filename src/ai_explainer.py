import re
from transformers import pipeline

# Initialize lightweight text generator
generator = pipeline("text-generation", model="distilgpt2")

def add_ai_explanations(report):
    """
    Add AI explanations to each detected issue in the report.
    """
    for issue in report:
        issue["ai_explanation"] = (
            f"Explain why using {issue['pattern']} in C++ could cause problems."
        )
    return report


def suggest_code_fix(issue_message):
    """
    Generate a clean, short, and readable C++ code fix for the issue.
    """
    prompt = f"Provide a corrected and safe C++ code example for this issue:\n{issue_message}\n\nC++ Code:\n"
    result = generator(prompt, max_length=120, num_return_sequences=1)
    suggestion = result[0]["generated_text"]

    # 🧹 Clean up output
    suggestion = re.sub(r"<.*?>", "", suggestion)
    suggestion = re.sub(r"[#@*]{2,}", "", suggestion)
    suggestion = re.sub(r"(\n\s*){2,}", "\n", suggestion)

    # Prevent overly long text
    if len(suggestion) > 400:
        suggestion = suggestion[:400] + "\n// ... truncated ..."

    return suggestion.strip()
