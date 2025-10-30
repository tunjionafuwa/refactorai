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

    colored_lines: list[str] = []
    for line in diff:
        if line.startswith("+") and not line.startswith("+++"):
            new_line = GREEN + line + RESET
        elif line.startswith("-") and not line.startswith("---"):
            new_line = RED + line + RESET 
        elif line.startswith("@@"):
            new_line = CYAN + line + RESET
        else:
            new_line = line
        colored_lines.append(new_line)
    return "".join(colored_lines)
