from pathlib import Path


def find_python_files(folder: str):
    return [p for p in Path(folder).rglob("*.py") if "venv" not in str(p)]

def read_file(filepath: str) -> str:
    with open(filepath, "r") as f:
        return f.read()
    
def write_file(filepath: str, content: str):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        