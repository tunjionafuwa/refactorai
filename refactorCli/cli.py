import argparse

from refactorCli.agents.code_editor import CodeEditorAgent
from dotenv import load_dotenv

load_dotenv()


def main():
    parser = argparse.ArgumentParser(
        description="LangChain-powered Python code reviewer and editor."
    )
    parser.add_argument("folder", help="Path to the folder containing Python files.")
    parser.add_argument(
        "--prompt",
        "-p",
        help="Custom review prompt.",
        default="Find and correct bugs or issues.",
    )
    parser.add_argument("--model", "-m", help="LLM model name", default="gpt-4o-mini")

    args = parser.parse_args()

    agent = CodeEditorAgent(model=args.model)
    agent.review_folder(args.folder, args.prompt)


# if __name__ == "__main__":
#     main()
