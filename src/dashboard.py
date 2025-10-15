import streamlit as st
import json
from src.parser import load_cpp_code
from src.analyzer import detect_issues
from src.reporter import print_console_report, save_json_report
from src.ai_explainer import add_ai_explanations, suggest_code_fix

# -------------------- Page Setup --------------------
st.set_page_config(page_title="AI-Powered C++ Code Reviewer (Offline)", layout="wide")
st.title("🤖 AI-Powered C++ Code Reviewer (Offline)")
st.markdown("Upload a **C++ source file** to analyze potential issues and view AI-generated explanations and fix suggestions.")

# -------------------- File Upload --------------------
uploaded_file = st.file_uploader("📂 Upload a .cpp file", type=["cpp"], help="Upload your C++ source code file for analysis.")

if uploaded_file:
    code = uploaded_file.read().decode("utf-8")
    st.code(code, language="cpp")

    if st.button("🚀 Run Analysis"):
        with st.spinner("Analyzing your C++ code..."):
            # Step 1: Analyze issues
            report = detect_issues(code)

            # Step 2: Add AI explanations
            report = add_ai_explanations(report)

            # Step 3: Save report
            save_json_report(report, out_path="reports/dashboard_result.json")

        # Step 4: Display results
        if report:
            st.subheader("🔍 Detected Issues")
            for i, issue in enumerate(report, start=1):
                st.markdown(f"### ⚠️ Issue {i}: {issue['type']}")
                st.markdown(f"**Pattern:** `{issue['pattern']}`")
                st.markdown(f"**Message:** {issue['message']}")

                if "ai_explanation" in issue:
                    st.info(f"**AI Explanation:** {issue['ai_explanation']}")

                # 🧠 New Feature — AI Fix Suggestion
                st.markdown("**💡 Suggested Code Fix:**")
                try:
                    fix = suggest_code_fix(issue["message"])
                    st.code(fix, language="cpp")
                except Exception as e:
                    st.warning(f"Unable to generate fix suggestion: {e}")

            st.success("✅ Report saved to `reports/dashboard_result.json`")

            # Step 5: Add Download Button
            try:
                with open("reports/dashboard_result.json", "r") as f:
                    json_data = f.read()

                st.download_button(
                    label="📥 Download Report",
                    data=json_data,
                    file_name="AI_Code_Review_Report.json",
                    mime="application/json"
                )
            except FileNotFoundError:
                st.warning("No report file found yet. Run analysis first.")
        else:
            st.info("✅ No issues detected. Great job!")
else:
    st.info("👆 Please upload a `.cpp` file to begin analysis.")
