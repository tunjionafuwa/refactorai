from refactorCli.llm.client import Client
from refactorCli.tools.file_utils import find_python_files, read_file, write_file
from refactorCli.utils.diff_utils import generate_diff


class CodeEditorAgent:
    def __init__(self, model:str="gpt-4o-mini"):
        self.llm_client = Client(model=model)

    def review_folder(self, folder: str, prompt: str):
        files = find_python_files(folder)
        for filepath in files:
            print(f"\n Reviewing {filepath}...")
            code = read_file(filepath=filepath)
            if not code.strip():
                print(f"Skipping empty file: {filepath}")
                continue

            suggestion = self.llm_client.review_code(code, filepath, prompt)

            if suggestion.strip() == code.strip():
                print("✅ No changes suggested.")
                continue

            diff = generate_diff(code, suggestion)
            print("\n--- Suggested Changes ---")
            print(diff)

            decision = input("\nApply changes? [y]es / [n]o / [s]kip all: ").strip().lower()
            if decision == "y":
                write_file(filepath, suggestion)
                print(f"Changes applied to {filepath}")
            elif decision == "s":
                print("Skipping remaining files.")
                break
            else:
                print("Skipped.")
