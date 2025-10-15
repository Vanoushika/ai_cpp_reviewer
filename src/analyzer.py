import re

def detect_issues(code: str):
    issues = []

    # 1️⃣ Unsafe functions
    unsafe_funcs = ["gets", "strcpy", "sprintf", "scanf"]
    for f in unsafe_funcs:
        if re.search(rf"\b{f}\s*\(", code):
            issues.append({
                "type": "Unsafe Function",
                "pattern": f,
                "message": f"'{f}' can cause buffer overflow. Use safer alternatives."
            })

    # 2️⃣ Unused variables
    # Find simple "int var;" declarations that never appear again
    decls = re.findall(r"\bint\s+(\w+)\s*;", code)
    for var in decls:
        uses = len(re.findall(rf"\b{var}\b", code))
        if uses == 1:
            issues.append({
                "type": "Unused Variable",
                "pattern": var,
                "message": f"Variable '{var}' declared but never used."
            })

    # 3️⃣ Potential memory leak (improved)
    # Detect 'new' allocations without any corresponding 'delete' or 'delete[]'
    new_calls = len(re.findall(r"\bnew\b", code))
    delete_calls = len(re.findall(r"\bdelete\b", code))
    if new_calls > delete_calls:
        issues.append({
            "type": "Potential Memory Leak",
            "pattern": "new/delete imbalance",
            "message": "Detected memory allocation using 'new' without a matching 'delete'."
        })

    # 4️⃣ Comment hint: detect when comments mention 'missing delete'
    if re.search(r"missing\s+delete", code, re.IGNORECASE):
        issues.append({
            "type": "Potential Memory Leak (Comment Hint)",
            "pattern": "missing delete",
            "message": "Comment suggests a missing delete[]. Possible memory leak."
        })

    return issues
