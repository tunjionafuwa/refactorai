import difflib

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
CYAN = "\033[96m"

def generate_diff(original: str, modified: str) -> str:
    """Generate a unified diff with colored +/− lines."""
    diff = difflib.unified_diff(
        original.splitlines(keepends=True),
        modified.splitlines(keepends=True),
        fromfile="original",
        tofile="suggested",
    )

    colored_lines = []
    for line in diff:
        if line.startswith("+") and not line.startswith("+++"):
            colored_lines.append(GREEN + line + RESET)
        elif line.startswith("-") and not line.startswith("---"):
            colored_lines.append(RED + line + RESET)
        elif line.startswith("@@"):
            colored_lines.append(CYAN + line + RESET)
        else:
            colored_lines.append(line)
    return "".join(colored_lines)
