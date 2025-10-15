from pathlib import Path

def load_cpp_code(file_path: str) -> str:
    """Reads a C++ file and returns its content as a string."""
    path = Path(file_path)
    return path.read_text(errors="ignore")
